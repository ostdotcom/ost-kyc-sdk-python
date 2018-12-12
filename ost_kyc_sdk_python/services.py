from .saas.manifest import Manifest

class Services:
    
    def __init__(self, params = {}):
        if not params.get('api_key'): raise Exception("missing API key")
        if  not params.get('api_secret'): raise Exception("missing API secret")
        if not  params.get('api_base_url'): raise Exception("missing endpoint")
        self.params = params
        self.set_menifest()


    def set_menifest(self):
        self.services = Manifest(self.params)


        



    
         