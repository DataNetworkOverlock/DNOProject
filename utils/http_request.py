import requests


class HttpRequest:
    def __init__(self, token):
        self.token = token
        self.base_url = 'http://datanetworkoverlock.live/'
        self.headers = {
            'Content-Type': 'application/json',
            'authorization': token
        }

    def make_request(self, method, url, payload=''):
        url = self.base_url + url
        if payload != '':
            request = requests.request(
                method, url, headers=self.headers, json=payload)
        else:
            request = requests.request(method, url, headers=self.headers)
        response = request.json()
        # response['status'] = request.status_code
        return {
            "response": response,
            "status": request.status_code
        }
