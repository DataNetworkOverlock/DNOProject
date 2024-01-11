import requests

class Tests:
    
    def __init__(self, token):
        self.token = token
        self.base_url = 'http://datanetworkoverlock.live/tests'
        self.headers = {
            'Content-Type': 'application/json',
            'authorization': token
        }

    def create_test(self, payload):
        url = self.base_url
        response = requests.request('POST', url, headers=self.headers, json=payload)
        return response.json()
    
    def get_tests_by_username(self, username):
        url = self.base_url + '/' + username
        response = requests.request('GET', url, headers=self.headers)
        return response.json()
