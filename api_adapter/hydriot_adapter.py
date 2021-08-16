import base64
import requests
import json
from datetime import datetime
from sensor import SensorUpdate

class HydriotAdapter():
    driver = None
    base_url = "https://hydriot.azurewebsites.net"
    headers = None

    def build_auth(self, username, password):
        raw = f"{username}:{password}"
        message_bytes = raw.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return base64_message

    def __init__(self, username, password) -> None:
        basic_auth = self.build_auth(username, password)
        
        self.headers = {
            'authorization': f"Basic {basic_auth}",
            'cache-control': "no-cache",
            'content-type': "application/json"
        }
    
    def check_if_device_is_registered(self, device_id):

        try:
            print("Making API call...")
            url = f"{self.base_url}/api/Device/CheckRegisteredStatus/{device_id}"
            response = requests.request("GET", url, headers=self.headers)

            if response.status_code != 200:
                raise LookupError(f'Failed to complete the request. Error Code [{response.status_code}]')

        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(f"Failed to verify registration. Error details >> {e}")
     
        return response.text == 'true'

    def register_device(self, name, description, createUpdate = False):

        payload = {
              "deviceName": name,
              "deviceDescription": description,
              "createUpdate": createUpdate
        }

        try:
            print("Making API call...")
            url = f"{self.base_url}/api/Device/RegisterDevice"
            response = requests.request("POST", url, data=json.dumps(payload), headers=self.headers)

            if response.status_code != 200:
                raise LookupError(f'Failed to complete the request. Error Code [{response.status_code}]')

        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(f"Failed to verify registration. Error details >> {e}")

        return response.json()

    def get_device_data(self, device_id):
        
        try:
            print("Making API call...")
            url = f"{self.base_url}/api/Device/GetDeviceData/{device_id}"
            response = requests.request("GET", url, headers=self.headers)

            if response.status_code != 200:
                raise LookupError(f'Failed to complete the request. Error Code [{response.status_code}]')

        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(f"Failed to verify registration. Error details >> {e}")

        return response.json()


    def update_sensor_data(self, device_id, name, description, sensors = []):
        sensor_update = SensorUpdate(device_id, name, description, sensors)

        ##TODO: Figure out how to serialize datetime to JSON
        payload = sensor_update.toJSON()
        
        try:
            print("Making API call...")
            url = f"{self.base_url}/api/Device/UpdateSensorData/{device_id}"
            response = requests.request("PUT", url, data=json.dumps(payload), headers=self.headers)

            if response.status_code != 200:
                raise LookupError(f'Failed to complete the request. Error Code [{response.status_code}]')

        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(f"Failed to verify registration. Error details >> {e}")

        return response.json()
     
        

