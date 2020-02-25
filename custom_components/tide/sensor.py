import logging
import xml.etree.ElementTree as ET

from collections import defaultdict
from datetime import timedelta

# from autologging import traced, TRACE
import pendulum
import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.const import ATTR_ATTRIBUTION, STATE_UNKNOWN
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.util import Throttle

from homeassistant.helpers.entity import Entity

from homeassistant.helpers.aiohttp_client import async_get_clientsession

from . import DOMAIN

_LOGGER = logging.getLogger(__name__)
# _LOGGER.setLevel(TRACE)

# What should be a good time for the updates?
MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=20)

# This should be float.
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional("lat", default=""): cv.string,
        vol.Optional("lon", default=""): cv.string,
    }
)


async def async_setup_platform(
    hass, config_entry, async_add_devices, discovery_info=None
):
    """Setup sensor platform for the ui"""
    config = config_entry
    api = TideAPI(config, hass)
    # await api.update()
    async_add_devices([TideSensor(api, hass, config)])
    return True


def to_data(data):
    root = ET.fromstring(data)
    data = defaultdict(dict)
    for el in root.iter("data"):
        for e in el:
            data[el.attrib.get("type")][e.attrib.get("time")] = e.attrib

    # Log any messages that the api might return i suddenly got
    # <service cominfo="Due to technical maintenance, the water level observations might be delayed from February 24 to February 28."/>
    for msg in root.iter("service"):
        _LOGGER.info("%s", msg.attrib.get("cominfo"))

    return data


def get_tide_xml_url(
    lat=58.974339,
    lon=5.730121,
    time_from=None,
    time_to=None,
    datatype="tab",
    interval=10,
):

    if time_from is None:
        time_from = pendulum.today()

    if time_to is None:
        time_to = pendulum.tomorrow().at(hour=23, minute=59, second=59)

    url = (
        f"http://api.sehavniva.no/tideapi.php?lat={lat}&lon={lon}&fromtime={time_from.isoformat()}"
        f"&totime={time_to.isoformat()}&datatype={datatype}&refcode=cd&place=&file=&lang=en&"
        f"interval={interval}&dst=0&tzone=0&tide_request=locationdata"
    )

    return url


class TideAPI:
    def __init__(self, config, hass):
        _LOGGER.info("Started api")
        self.lat = config.get("lat")
        self.lon = config.get("lon")
        # the rest of the settings is hard coded for now.
        self.datatype = "tab"
        self.interval = config.get("interval", 10)
        self.data = None
        self._hass = hass

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    async def fetch(self):
        _LOGGER.info("tide api fetch")
        url = get_tide_xml_url(
            self.lat, self.lon, datatype=self.datatype, interval=self.interval
        )
        data = None
        _LOGGER.info(url)
        sess = async_get_clientsession(self._hass)
        result = await sess.get(url)
        if result:
            res = await result.text()
            _LOGGER.info(result.status)
            _LOGGER.info(res)
            data = to_data(res)
            self.data = data

        _LOGGER.info(data)

    async def update(self):
        _LOGGER.info("tide api update")
        await self.fetch()


# @traced
class TideSensor(Entity):
    def __init__(self, api, hass, config):
        _LOGGER.info("started sensorz.")
        self._api = api
        self._hass = hass
        self._config = config
        self.attributes = {ATTR_ATTRIBUTION: "kartverket"}
        _LOGGER.info(config)
        self._state = STATE_UNKNOWN

    async def async_update(self):
        _LOGGER.info("called update")
        await self._real_update()

    async def _real_update(self):
        _LOGGER.info("called _update")
        await self._api.update()
        now = pendulum.now()
        d = self._api.data.get("prediction", {})
        sorted_times = {k: d[k] for k in sorted(d)}
        _LOGGER.info(sorted_times)
        for key, value in sorted_times.items():
            _LOGGER.info(value)
            key = pendulum.parse(key)
            if now > key:
                _LOGGER.info("Found %s", now)
                self._state = value.get("flag")
                self.attributes["water_level"] = value.get("value")
                break

    @property
    def icon(self) -> str:
        """Shows the correct icon for container."""
        # todo fix icons.
        return "mdi:water"

    @property
    def state(self):
        return self._state

    @property
    def unique_id(self) -> str:
        """Return the name of the sensor."""
        return f'tide_{self._config.get("lat")}_{self._config.get("lon")}'

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
    def unit(self) -> int:
        """Unit"""
        return int

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement this sensor expresses itself in."""
        return "cm"
