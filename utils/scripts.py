from utils.http_request import HttpRequest

class Scripts(HttpRequest):

    def __init__(self, token):
        super().__init__(token)
    
    def get_scripts(self):
        url = 'scripts'
        return self.make_request('GET', url)
