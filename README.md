# Powerwall 2 Stats

The library powerwallstats provides a simple class to access a
Powerwall 2 directly from your local Powerwall gateway, not Tesla's
cloud.

## To install

pip install powerwallstats

## Example of use

[examples/show_powerwallstats.py](examples/show_powerwallstats.py)
provides a simple example use case.  You will need need to setup
customer email and password information on your Powerwall: follow the
[Tesla documentation](https://www.tesla.com/en_gb/support/energy/powerwall/own/monitoring-from-home-network)
to do this.

## Testing status

This has been tested on 4th March 2021 against a Powerwall 2 running
firmware version 20.49.0 that requires customer login credentials to
be presented.  Tested using python3.

## References

Alas Tesla do not appear to have released API documentation to
customers, which seems short sighted.  Details of the Tesla gateway
API have been reverse engineered and further details are available
from
[https://github.com/vloschiavo/powerwall2](https://github.com/vloschiavo/powerwall2)

