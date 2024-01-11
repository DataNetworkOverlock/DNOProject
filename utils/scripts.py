import requests

class Scripts:
    def __init__(self, token):
        self.token = token
        self.base_url = 'http://datanetworkoverlock.live/scripts'
        self.headers = {
            'Content-Type': 'application/json',
            'authorization': token
        }
    
    def get_scripts(self):
        url = self.base_url
        response = requests.request('GET', url, headers=self.headers)
        return response.json();