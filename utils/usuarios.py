import requests

class Usuarios:

    def __init__(self, token=''):
        self.token = token
        self.base_url = 'http://datanetworkoverlock.live/'
        self.headers = {
            'Content-Type': 'application/json',
            'authentication': token
        }

    def create_user(self, payload):
        url = self.base_url + 'users'
        response = requests.request('POST', url, headers=self.headers, json=payload)
        return response.json()

    def login(self, payload):
        url = self.base_url + 'login'
        response = requests.request('POST', url, headers=self.headers, json=payload)
        return response.json()
