"""Daikin Modbus custom integration."""

from .vendor.daikin_modbus import DaikinAidoo

from homeassistant.components.modbus import async_get_unit
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from modbus_connection import ModbusTcpParams

from .const import CONF_HOST, CONF_PORT, CONF_UNIT_ID
from .coordinator import DaikinCoordinator

PLATFORMS = [Platform.CLIMATE, Platform.SENSOR]
type DaikinConfigEntry = ConfigEntry[DaikinCoordinator]


async def async_setup_entry(hass: HomeAssistant, entry: DaikinConfigEntry) -> bool:
    """Set up the Daikin Modbus integration."""
    unit = async_get_unit(
        hass,
        entry,
        ModbusTcpParams(
            host=entry.data[CONF_HOST],
            port=int(entry.data[CONF_PORT]),
        ),
        int(entry.data[CONF_UNIT_ID]),
    )
    device = DaikinAidoo(unit)
    coordinator = DaikinCoordinator(hass, entry, device)
    await coordinator.async_config_entry_first_refresh()
    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: DaikinConfigEntry) -> bool:
    """Unload the integration."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
