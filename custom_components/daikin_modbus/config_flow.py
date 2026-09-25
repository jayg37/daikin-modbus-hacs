"""Config flow for Daikin Modbus."""

from typing import Any

import voluptuous as vol
from modbus_connection import ModbusError, ModbusTcpParams

from homeassistant.components.modbus import async_get_temporary_unit
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.helpers.selector import (
    NumberSelector,
    NumberSelectorConfig,
    NumberSelectorMode,
)

from .const import (
    CONF_HOST,
    CONF_PORT,
    CONF_UNIT_ID,
    DEFAULT_HOST,
    DEFAULT_PORT,
    DEFAULT_UNIT_ID,
    DOMAIN,
)
from .vendor.daikin_modbus import DaikinAidoo

STEP_USER = vol.Schema(
    {
        vol.Required(CONF_HOST, default=DEFAULT_HOST): str,
        vol.Required(CONF_PORT, default=DEFAULT_PORT): NumberSelector(
            NumberSelectorConfig(
                min=1,
                max=65535,
                step=1,
                mode=NumberSelectorMode.BOX,
            )
        ),
        vol.Required(CONF_UNIT_ID, default=DEFAULT_UNIT_ID): NumberSelector(
            NumberSelectorConfig(
                min=1,
                max=247,
                step=1,
                mode=NumberSelectorMode.BOX,
            )
        ),
    }
)


class DaikinModbusConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle setup."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the user setup step."""
        errors: dict[str, str] = {}

        if user_input is not None:
            host = str(user_input[CONF_HOST])
            port = int(user_input[CONF_PORT])
            unit_id = int(user_input[CONF_UNIT_ID])

            await self.async_set_unique_id(f"{host}:{port}:{unit_id}")
            self._abort_if_unique_id_configured()

            data = {
                CONF_HOST: host,
                CONF_PORT: port,
                CONF_UNIT_ID: unit_id,
            }

            if await self._async_validate(data):
                return self.async_create_entry(title="Daikin Modbus", data=data)

            errors["base"] = "cannot_connect"

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER,
            errors=errors,
        )

    async def _async_validate(self, data: dict[str, Any]) -> bool:
        """Validate the Modbus connection and Daikin device."""
        params = ModbusTcpParams(
            host=str(data[CONF_HOST]),
            port=int(data[CONF_PORT]),
        )

        try:
            async with async_get_temporary_unit(
                self.hass, params, int(data[CONF_UNIT_ID])
            ) as unit:
                await DaikinAidoo(unit).async_update()
        except (ModbusError, OSError, ValueError):
            return False

        return True
