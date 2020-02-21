from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
from collections import defaultdict

import logging

from datetime import datetime as DT
from datetime import datetime, timedelta


import pendulum

from . import DOMAIN
import pendulum


import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_REGION
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity
from homeassistant.const import ATTR_ATTRIBUTION
from homeassistant.helpers.aiohttp_client import async_get_clientsession

_LOGGER = logging.getLogger(__name__)
MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=20)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional("lat", default=""): cv.string,
        vol.Optional("lon", default=""): cv.string,
    }
)


def to_data(data):
    root = ET.fromstring(data)
    data = defaultdict(dict)
    for el in root.iter('data'):
        for e in el:
            data[el.attrib.get('type')][e.attrib.get("time")] = e.attrib
    return data


def get_tide_xml_url(lat=58.974339, lon=5.730121, time_from=None, time_to=None, datatype="tab", interval=10):

    if time_from is None:
        time_from = datetime.utcnow().replace(second=0, microsecond=0)

    if time_to is None:
        time_to = time_from + timedelta(hours=24)
        time_to.replace(second=0, microsecond=0)

    url = (f"http://api.sehavniva.no/tideapi.php?lat={lat}&lon={lon}&fromtime={time_from.isoformat()}"
           "&totime={time_to.isoformat()}&datatype={datatype}&refcode=cd&place=&file=&lang=en&"
           "interval={interval}&dst=0&tzone=0&tide_request=locationdata")

    return url



class TideAPI():
    def __init__(self,  config, hass):
        self.lat = config.get("lat")
        self.lon = config.get("lon")
        self.datatype = "tab"
        self.interval = config.get("interval")
        self.data = None
        self._hass = hass

        self.attribibutes = {}

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    async def fetch(self):
        url = get_tide_xml_url(self.lat, self.lon, datatype=self.datatype, interval=self.interval)

        sess = async_get_clientsession(self._hass)
        async with sess:
            result = await sess.get(url)
            if result:
                data = to_data(result.text)
                self.data = data


class TideSensor(Entity):
    def __init__(self, api, hass, config):
        self._api = api
        self._hass = hass
        self._config = config
        self.attribibutes = {ATTR_ATTRIBUTION: "kartverket"}

    async def update(self):
        await self._update()

    async def _update(self):
        now = DT.utcnow()
        sorted_times = sorted(self.data.get("prediction", {}))
        for key, value in sorted_times.items():
            key = pendulum.parse(key)
            if now > key:
                self._state = value.get("flag")
                self.attribibutes["water_level"] = value.get("value")
                break

    @property
    def icon(self) -> str:
        """Shows the correct icon for container."""
        # todo fix icons.
        return "mdi:water"

    @property
    def unique_id(self) -> str:
        """Return the name of the sensor."""
        return f'tide_{self.config.get("lat")}_{self.config.get("lon")}'

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
    def unit(self)-> int:
        """Unit"""
        return int

    @property
    def unit_of_measurement(self) -> str:
        """Return the unit of measurement this sensor expresses itself in."""
        return "cm"




"""
defaultdict(<class 'dict'>, {'prediction': {'2020-02-22T02:38:00+00:00': {'value': '46.0', 'time': '2020-02-22T02:38:00+00:00', 'flag': 'low'}, '2020-02-22T08:48:00+00:00': {'value': '87.0', 'time': '2020-02-22T08:48:00+00:00', 'flag': 'high'}, '2020-02-22T15:04:00+00:00': {'value': '40.8', 'time': '2020-02-22T15:04:00+00:00', 'flag': 'low'}, '2020-02-22T21:15:00+00:00': {'value': '85.8', 'time': '2020-02-22T21:15:00+00:00', 'flag': 'high'}}})
"""
