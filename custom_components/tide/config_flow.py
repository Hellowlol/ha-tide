"""Adds config flow for tide."""

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import ATTR_ATTRIBUTION, CONF_LATITUDE, CONF_LONGITUDE

from . import DOMAIN


@config_entries.HANDLERS.register(DOMAIN)
class TideFlowHandler(config_entries.ConfigFlow):
    """Config flow for Tide."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    def __init__(self):
        """Initialize."""
        self._errors = {}

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""

        if user_input is not None:
            return self.async_create_entry(
                title="Tide", data=user_input)

        return self.async_show_form(step_id="user", data_schema=vol.Schema({
            vol.Required(CONF_LATITUDE,
                         default=1.0): vol.Coerce(float),
            vol.Required(CONF_LONGITUDE,
                         default=1.0): vol.Coerce(float)
        }), errors=self._errors)

    async def async_step_import(self, user_input=None):
        """Import a config flow from configuration."""
        return self.async_create_entry(title="configuration.yaml", data={})
