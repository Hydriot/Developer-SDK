import base64
import requests

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
            'postman-token': "cd202212-8067-4a22-a1f0-3bedbcc13ef8"
        }
    
    def check_if_device_is_registered(self, deviceId):

        try:
            print("Making API call...")
            url = f"{self.base_url}/api/Device/CheckRegisteredStatus/{deviceId}"
            response = requests.request("GET", url, headers=self.headers)

            if response.status_code != 200:
                raise LookupError(f'Failed to complete the request. Error Code [{response.status_code}]')

        except requests.exceptions.RequestException as e:  # This is the correct syntax
            print(f"Failed to verify registration. Error details >> {e}")
     
        return response.text == 'true'





     
        

