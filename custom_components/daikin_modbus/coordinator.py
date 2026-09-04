"""Coordinator."""

import logging

from modbus_connection import ModbusError

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN, SCAN_INTERVAL
from .vendor.daikin_modbus import DaikinAidoo

_LOGGER = logging.getLogger(__name__)
type DaikinConfigEntry = ConfigEntry["DaikinCoordinator"]


class DaikinCoordinator(DataUpdateCoordinator[DaikinAidoo]):
    """Poll the vendorized Daikin device model."""

    def __init__(self, hass: HomeAssistant, entry: DaikinConfigEntry, device: DaikinAidoo) -> None:
        super().__init__(hass, _LOGGER, name=DOMAIN, config_entry=entry, update_interval=SCAN_INTERVAL)
        self.device = device

    async def _async_update_data(self) -> DaikinAidoo:
        try:
            await self.device.async_update()
        except (ModbusError, OSError, ValueError) as err:
            raise UpdateFailed(f"Error communicating with Daikin: {err}") from err
        return self.device
