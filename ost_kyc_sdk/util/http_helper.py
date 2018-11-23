import hashlib, hmac, urllib
import collections
import requests
import time
import json
from .python_version import python_version

#
# HTTPHelper class used by SDK services to communicate with given endpoints
# * Author: Mayur
# * Date: 19/11/2018
# * Reviewed By:
#
class HTTPHelper:

    def __init__(self, params):
        self.api_key = params.get('api_key')
        self.api_secret = params.get('api_secret')
        self.api_base_url = params.get('api_base_url')
        self.urlencode = urllib.urlencode  if python_version() == 2 else urllib.parse.urlencode    

    # 
    # Send post request to specified endpoint with given request params 
    # * Author: Mayur
    # * Date: 19/11/2018
    # * Reviewed By:
    #
    # @return dict
    #    
    def send_post_request(self, endpoint, request_params):
        request_params.update(self.get_base_params(endpoint, request_params))
        qs = self.dict_to_urlencoded(request_params) 
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post (self.get_api_url(endpoint), data = qs, headers=headers, timeout=15, verify=self.verify_required() ) 
        try:
            return response.json()
        except:
            return {"success":False,"err":{"code":"SOMETHING_WENT_WRONG","internal_id":"SDK(SOMETHING_WENT_WRONG)","msg":"","error_data":[]}}


    #    
    # Check if verify required for requests
    # 
    # * Author: Mayur
    # * Date: 19/11/2018
    # * Reviewed By:
    #
    # @return dict
    #  
    def verify_required(self):
        if self.urlparse()(self.api_base_url).scheme == "http":
            return True
        return True             
            

    #    
    # Send get request to specified endpoint with given request params 
    # 
    # * Author: Mayur
    # * Date: 19/11/2018
    # * Reviewed By:
    #
    # @return dict
    #        
    def send_get_request(self, endpoint, request_params):
        request_params.update(self.get_base_params(endpoint, request_params))
        qs = self.dict_to_urlencoded(request_params)
        response = requests.get(self.get_api_url(endpoint) + "?" + qs, timeout=15 )
        try:
            return response.json()
        except:
            return {"success":False,"err":{"code":"SOMETHING_WENT_WRONG","internal_id":"SDK(SOMETHING_WENT_WRONG)","msg":"","error_data":[]}}


    #    
    # Get base params required for each request
    # 
    # * Author: Mayur
    # * Date: 19/11/2018
    # * Reviewed By:
    #
    # @return dict
    # 
    def get_base_params(self, endpoint, request_params):
        request_timestamp = int(time.time())
        request_params.update({"request_timestamp": request_timestamp, "api_key": self.api_key})
        request_params_str = self.dict_to_urlencoded(request_params)
        string_to_sign = endpoint + "?" + request_params_str
        signature = self.generate_signature(string_to_sign)
        return {"request_timestamp": request_timestamp, "signature": signature, "api_key": self.api_key} 
    
    #    
    # Get api url base_url + endpoint 
    # 
    # * Author: Mayur
    # * Date: 19/11/2018
    # * Reviewed By:
    #
    # @return dict
    # 
    def get_api_url(self, endpoint):
        return self.api_base_url + endpoint

 
    #    
    # Returns query string generated using given dictionary d
    # 
    # * Author: Mayur
    # * Date: 19/11/2018
    # * Reviewed By:
    #
    # @return str
    #     
    def dict_to_urlencoded(self, d):
        #return self.kv_translation(d, "", "")[:-1]
        d = self.sort_dict(d) #collections.OrderedDict(sorted(d.items()))
        return self.build_nested_query(d)



    #    
    # Returns sorted ordereddict
    # 
    # * Author: Mayur
    # * Date: 19/11/2018
    # * Reviewed By:
    #
    # @return dict
    #  
    def sort_dict(self, od):
        res = collections.OrderedDict()
        for k, v in sorted(od.items()):
            if isinstance(v, dict):
                res[k] = self.sort_dict(v)
            else:
                res[k] = v
        return res
     

    #    
    # Generate signature from api secret and string to sign 
    # 
    # * Author: Mayur
    # * Date: 19/11/2018
    # * Reviewed By:
    #
    # @return str
    # 
    def generate_signature(self, string_to_sign, api_secret=None):
        api_secret = api_secret.encode('utf-8') if api_secret else  self.api_secret.encode('utf-8') 
        string_to_sign = string_to_sign.replace('~', '%7E') 
        return hmac.new(api_secret, string_to_sign.encode('utf-8'),  hashlib.sha256).hexdigest()

    #    
    # Urlencodes given input 
    # 
    # * Author: Mayur
    # * Date: 22/11/2018
    # * Reviewed By:
    #
    # @return str
    # 
    def build_nested_query(self, value, prefix = None ):
        #case value
        if type(value) is list:  
          return "&".join([ self.build_nested_query(list_val, prefix+"[]") for list_val in value])
        elif isinstance(value, dict):
            d_list = []
            for key in value:
                d_list.append(self.build_nested_query(value[key], prefix + "[" + key + "]" if prefix else key ))
            return "&".join(filter(None, d_list)) 
        elif not value:
            return prefix + '='  
        else:
            return self.urlencode({prefix:value})


    #    
    # generate signature for testing 
    # 
    # * Author: Mayur
    # * Date: 22/11/2018
    # * Reviewed By:
    #
    # @return str
    # 
    def get_signature_for_test(self, di, endpoint, api_secret):
        request_params_str = self.dict_to_urlencoded(di)
        string_to_sign = endpoint + "?" + request_params_str
        return self.generate_signature(string_to_sign, api_secret)



    def urlparse(self):
        if python_version() == 2:
            import urlparse
            return urlparse.urlparse
        else:
            return urllib.parse.urlparse

