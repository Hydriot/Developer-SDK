
import json
from enum import IntEnum
from datetime import datetime

class BaseType(IntEnum):
    Undefined = 0
    String = 1
    Integer = 2
    Decimal = 3

class SensorType(IntEnum):
    Undefined = 0
    WaterLevel = 1
    TDS = 2
    pH = 3
    LightFrequency = 4
    LightIntensity = 5
    Custom = 99

class Settings():
    BaseType = None
    LowerBound = None
    UpperBound = None

    def __init__(self, base_type, lower_bound, upper_bound):
        self.BaseType = base_type
        self.LowerBound = lower_bound
        self.UpperBound = upper_bound

class Sensor():
    value = None
    type = None
    readTime = None
    name = None
    reference = None
    isAvailble = True
    isHealthy = True
    groupName = None
    settings = None

    def __init__(self, type, value, name = str(type), read_time = datetime.now(), group_name = 'default', settings = None):
        self.name = name
        self.value = value
        self.type = type
        self.readTime = read_time
        self.groupName = group_name
        self.settings = settings
      
class SensorUpdate():

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    deviceId = None
    name = None
    description = None
    sensors = None

    def __init__(self, deviceId, name, description, sensors = []):
        self.deviceId = deviceId
        self.name = name
        self.description = description
        self.sensors = sensors

