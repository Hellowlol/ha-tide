import logging

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "tide"

_LOGGER = logging.getLogger(__name__)

NAME = DOMAIN
VERSION = "0.0.3"
ISSUEURL = "https://github.com/hellowlol/ha-tide/issues"

STARTUP = """
-------------------------------------------------------------------
{name}
Version: {version}
This is a custom component
If you have any issues with this you need to open an issue here:
{issueurl}
-------------------------------------------------------------------
""".format(
    name=NAME, version=VERSION, issueurl=ISSUEURL
)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up this component using YAML."""
    _LOGGER.info(STARTUP)
    if config.get(DOMAIN) is None:
        # We get her if the integration is set up using config flow
        return True

    try:
        await hass.config_entries.async_forward_entry(config, "sensor")
    except ValueError:
        pass

    hass.async_create_task(
        hass.config_entries.flow.async_init(
            DOMAIN, context={"source": config_entries.SOURCE_IMPORT}, data={}
        )
    )
    return True


async def async_setup_entry(
    hass: HomeAssistant, entry: config_entries.ConfigEntry
) -> bool:
    """Set up tide as config entry."""

    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True


async def async_unload_entry(
    hass: HomeAssistant, entry: config_entries.ConfigEntry
) -> bool:
    """Unload a config entry."""
    await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    return True
