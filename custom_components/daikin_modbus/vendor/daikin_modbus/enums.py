"""Enumerations for the vendored Aidoo model."""
from enum import IntEnum

class HvacMode(IntEnum):
    AUTO = 1
    COOL = 2
    HEAT = 3
    FAN = 4
    DRY = 5

class FanSpeed(IntEnum):
    AUTO = 0
    SPEED_1 = 1
    SPEED_2 = 2
    SPEED_3 = 3

class LouverMode(IntEnum):
    POSITION_0 = 0
    POSITION_1 = 1
    POSITION_2 = 2
    POSITION_3 = 3
    POSITION_4 = 4
    POSITION_5 = 5
    POSITION_6 = 6
    POSITION_7 = 7
    AUTO = 8
    SWING = 9
    SWIRL = 10
