# Daikin Modbus

Custom Home Assistant integration for Daikin/Airzone Aidoo Modbus devices.

This repository is the community-testable version of the Daikin Modbus integration. It follows the same architecture intended for Home Assistant core, but vendors the standalone `daikin-modbus` device library inside the integration so HACS installation does not require a separately published Python package.

## Requirements

- Home Assistant with the new `modbus_connection` integration available.
- A Modbus TCP connection to a TCP-to-RS485 gateway such as the Elfin EW11.
- Aidoo/Daikin Modbus unit ID, normally `1` for the tested installation.

## Installation

Install through HACS as a custom repository, then restart Home Assistant. Add **Daikin Modbus** from Settings > Devices & services and select the existing Modbus connection.

## Hardware architecture

```text
Daikin → Airzone Aidoo → RS485 → Elfin EW11 → Modbus TCP → Home Assistant
```

The integration does not communicate with the gateway using MQTT. The EW11 is used as a Modbus TCP to RTU bridge.

## Current register support

Verified writable registers:

- 0: power
- 1: temperature setpoint (°F × 10)
- 3: HVAC mode
- 54: numeric fan speed

Verified read-only register:

- 2: room temperature (°F × 10)

The complete documented register map is included in the vendored device library. Registers that have not been tested are read-only.

## Development status

This is a community testing repository and is intended to validate the device model and Home Assistant integration before proposing the integration to Home Assistant core.
