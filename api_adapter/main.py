import json
from hydriot_adapter import HydriotAdapter
from sensor import Sensor, Settings, SensorType, BaseType

## =============================================================
adapter = HydriotAdapter('XXXX','XXXX')
device_id = 'A31AAB65-A798-41F1-952D-EFA47AD1CC71'
## =============================================================

def check_if_registered():
    is_registered = adapter.check_if_device_is_registered(device_id)
    return f"Status >> {'Device is registered' if is_registered else 'Device is NOT registered' }"

def register_device():
    newDevice = adapter.register_device('Test Device','Seed example device', True)
    return f"Device is registered to [{newDevice}]"

def get_device_data():
    deviceData = adapter.get_device_data(device_id)
    return deviceData

def update_sensor_data():

    sensor_list = [
        Sensor(SensorType.pH, 6),
        Sensor(SensorType.TDS, 154)
    ]

    deviceData = adapter.update_sensor_data(device_id, 'Test Device', 'Seed example device', sensor_list)
    return deviceData

print (update_sensor_data())