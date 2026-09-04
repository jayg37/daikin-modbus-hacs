# Contributing

This repository is the community-testing stage for the Daikin Modbus Home Assistant integration.

## Before changing protocol behavior

Do not make a register writable unless its behavior has been verified against the Aidoo/Daikin hardware. Update the register map documentation and tests when new behavior is confirmed.

## Development

Use `scripts/setup` to create the development environment and `scripts/develop` to launch Home Assistant with the custom component loaded.

Run `scripts/lint` before submitting changes.
