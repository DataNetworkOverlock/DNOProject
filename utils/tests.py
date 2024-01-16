from utils.http_request import HttpRequest

class Tests(HttpRequest):
    
    def __init__(self, token):
        super().__init__(token)

    def create_test(self, payload):
        url = 'tests'
        return self.make_request('POST', url, payload)
    
    def get_tests_by_username(self, username):
        url = 'tests/{username}'
        return self.make_request('GET', url)
