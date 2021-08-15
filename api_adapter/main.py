from hydriot_adapter import HydriotAdapter

## =============================================================
adapter = HydriotAdapter('XXX','XXX')
## =============================================================

## Check if device is registered
## ----------------------------------------------------------------------------------------
is_registered = adapter.check_if_device_is_registered('A31AAB65-A798-41F1-952D-EFA47AD1CC71')
print (f"Status >> {'Device is registered' if is_registered else 'Device is NOT registered' }")
