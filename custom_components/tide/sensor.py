import logging
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import timedelta

import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (ATTR_ATTRIBUTION, CONF_LATITUDE,
                                 CONF_LONGITUDE, STATE_UNKNOWN)
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle
from homeassistant.util import dt as dt_utils

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)
HIGH_LOW_TO_STATE = {"high": "Ebb", "low": "Flow"}
# What should be a good time for the updates?
MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=20)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_LATITUDE, default=""): cv.latitude,
        vol.Required(CONF_LONGITUDE, default=""): cv.longitude,
    }
)


async def async_setup_platform(
    hass, config_entry, async_add_devices, discovery_info=None
) -> True:
    """Setup sensor platform for the ui"""
    config = config_entry
    api = TideAPI(config, hass)
    async_add_devices([TideSensor(api, hass, config)])
    return True


async def async_setup_entry(hass, config_entry, async_add_devices):
    """Setup sensor platform for the ui"""
    return await async_setup_platform(
        hass, config_entry.data, async_add_devices, discovery_info=None
    )


async def async_remove_entry(hass, config_entry):
    try:
        await hass.config_entries.async_forward_entry_unload(config_entry, "sensor")
        _LOGGER.info("Successfully tide integration")
    except ValueError:
        pass


def to_data(data) -> dict:
    root = ET.fromstring(data)
    data = defaultdict(dict)
    for el in root.iter("data"):
        for e in el:
            data[el.attrib.get("type")][e.attrib.get("time")] = e.attrib

    # Log any messages that the api might return i suddenly got
    # <service cominfo="Due to technical maintenance, the water level observations might be delayed from February 24 to February 28."/>
    for msg in root.iter("service"):
        # Lets use a warning here as no good comes
        # from cominfo anyway. Just want a warning to to easier to
        # find in the logs for the users.
        _LOGGER.warning("%s", msg.attrib.get("cominfo"))

    for location in root.iter("location"):
        data["location"] = location.attrib

    for err in root.iter("error"):
        _LOGGER.warning("%s", err.text)

    return data


def get_tide_xml_url(
    lat=58.974339,
    lon=5.730121,
    time_from=None,
    time_to=None,
    datatype="tab",
    interval=10,
) -> str:

    if time_from is None:
        time_from = dt_utils.start_of_local_day()
        time_from_str = time_from.strftime("%Y-%m-%dT%H:%M:%S.%f%z")

    if time_to is None:
        time_to = dt_utils.start_of_local_day() + timedelta(days=1, hours=23, minutes=59, seconds=59)
        time_to_str = time_to.strftime("%Y-%m-%dT%H:%M:%S.%f%z")

    url = (
        f"http://vannstand.kartverket.no/tideapi.php?lat={lat}&lon={lon}&fromtime={time_from_str}"
        f"&totime={time_to_str}&datatype={datatype}&refcode=cd&place=&file=&lang=en&"
        f"interval={interval}&dst=0&tzone=1&tide_request=locationdata"
    )

    return url


class TideAPI:
    def __init__(self, config, hass):
        # http://vannstand.kartverket.no/tideapi_protocol.pdf
        self.lat = config.get("latitude")
        self.lon = config.get("longitude")
        # the rest of the settings is hard coded for now.
        self.datatype = "tab"
        self.interval = config.get("interval", 10)
        self.data = defaultdict(dict)
        self._hass = hass

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    async def _fetch_ebb_and_flow(self) -> None:
        """Fetches the url updates the data."""
        _LOGGER.debug("tide api fetch")
        url = get_tide_xml_url(
            self.lat, self.lon, datatype=self.datatype, interval=self.interval
        )
        data = None
        _LOGGER.debug(url)
        sess = async_get_clientsession(self._hass)
        result = await sess.get(url)
        res = await result.text()
        if result and result.status == 200:
            _LOGGER.debug(result.status)
            _LOGGER.debug(res)
            try:
                data = to_data(res)
                self.data["ebb_and_flow"] = data
            except ET.ParseError:
                _LOGGER.warning("Failed to read the xml, response was %s", res)
        else:
            _LOGGER.warning(
                "Didnt get a proper response from the api status code %s %s",
                result.status,
                res,
            )

    async def update(self) -> None:
        _LOGGER.debug("requested update")
        await self._fetch_ebb_and_flow()

    def ebb_and_flow(self) -> dict:
        return self.data.get("ebb_and_flow", {})


class TideSensor(Entity):
    def __init__(self, api, hass, config):
        _LOGGER.debug(config)
        self._api = api
        self._hass = hass
        self._config = config
        self.attributes = {ATTR_ATTRIBUTION: "kartverket"}
        self._state = STATE_UNKNOWN

    async def async_update(self) -> None:
        await self._real_update()

    async def _real_update(self) -> None:
        await self._api.update()
        data = self._api.ebb_and_flow()
        d = data.get("prediction", {})

        # Set the correct data for the requested location
        # using the known offset from the measurement station.
        sorted_times = {k: d[k] for k in sorted(d, reverse=True)}
        fixed_data = defaultdict(dict)
        delay = int(data.get("location", {}).get("delay", 0))
        factor = float(data.get("location", {}).get("factor", 1))

        for key, value in sorted_times.items():
            key = dt_utils.parse_datetime(key)
            key = key + timedelta(minutes=delay)
            dt_as_str = str(key)
            val = float(value.get("value")) * factor
            fixed_data[dt_as_str]["flag"] = value.get("flag")
            fixed_data[dt_as_str]["value"] = val
            fixed_data[dt_as_str]["time"] = dt_as_str

        for fixed_key, fixed_value in fixed_data.items():
            if dt_utils.now() > dt_utils.parse_datetime(fixed_key):
                _LOGGER.debug("Selected %r as current values for state and attributes", fixed_value)
                self._state = HIGH_LOW_TO_STATE[fixed_value.get("flag")]
                self.attributes["high_water"] = (
                    True if fixed_value.get("flag") == "high" else False
                )
                self.attributes.update(data.get("location", {}))
                self.attributes["water_level"] = fixed_value.get("value")
                self.attributes["water_levels"] = list(reversed(list(fixed_data.values())))
                self.attributes["station_name"] = self.attributes["name"]
                del self.attributes["name"]
                break

    @property
    def icon(self) -> str:
        """Just a icon."""
        return "mdi:wave"

    @property
    def state(self) -> str:
        """State of the sensor"""
        return self._state

    @property
    def unique_id(self) -> str:
        """Return the name of the sensor."""
        return f'tide_{self._config.get("latitude")}_{self._config.get("longitude")}'.replace(
            ".", "_"
        )

    @property
    def name(self) -> str:
        return self.unique_id

    @property
    def device_state_attributes(self) -> dict:
        """Return the state attributes."""
        return self.attributes

    @property
    def device_info(self) -> dict:
        """I can't remember why this was needed :D"""
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": self.name,
            "manufacturer": DOMAIN,
        }

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement this sensor expresses itself in."""
        return "cm"
