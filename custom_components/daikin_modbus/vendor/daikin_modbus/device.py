"""Vendored Daikin/Airzone Aidoo Modbus model."""

from modbus_connection.model import Component, boolean, enum, gauge, integer, raw_register

from .enums import HvacMode


class DaikinAidoo(Component):
    """Model the documented runtime register map."""

    register_ranges = ((0, 5), (14, 15), (54, 55))

    power = boolean(0, writable=True)
    setpoint = gauge(1, 0.1, signed=False, writable=True, unit="°F")
    room_temperature = gauge(2, 0.1, signed=False, unit="°F")
    hvac_mode = enum(3, HvacMode, writable=True)
    fan_percentage = integer(4, signed=False, unit="%")
    louver = integer(5, signed=False)
    available_modes = raw_register(14)
    available_speeds = raw_register(15)
    fan_speed = integer(54, signed=False, writable=True)
