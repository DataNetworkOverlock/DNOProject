from utils.http_request import HttpRequest

class Usuarios(HttpRequest):

    def __init__(self, token=''):
        super().__init__(token)

    def create_user(self, payload):
        url = 'users'
        return self.make_request('POST', url, payload)

    def login(self, payload):
        url = 'login'
        return self.make_request('POST', url, payload)
