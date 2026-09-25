"""Constants."""

from datetime import timedelta

DOMAIN = "daikin_modbus"
CONF_HOST = "host"
CONF_PORT = "port"
CONF_UNIT_ID = "unit_id"
DEFAULT_HOST = "192.168.1.29"
DEFAULT_PORT = 502
DEFAULT_UNIT_ID = 1
SCAN_INTERVAL = timedelta(seconds=30)
