
import os
import hashlib, hmac, urllib
import collections
import requests
import time
import json
from .python_version import python_version
import re

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
        self.config = params.get('config') or {}
        self.timeout = self.config.get('timeout') or 15
        self.urlencode = urllib.urlencode  if python_version() == 2 else urllib.parse.urlencode
        self.urlparse()    

    # 
    # Send post request to specified endpoint with given request params 
    # * Author: Mayur
    # * Date: 19/11/2018
    # * Reviewed By:
    #
    # @return dict
    #    
    def send_post_request(self, endpoint, request_params):
        qs = self.get_query_string_with_base_params(endpoint, request_params)
        qs = self.parse_url(qs).query
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        try:
            response = requests.post (self.get_api_url(endpoint), data = qs, headers=headers, timeout=self.timeout, verify=self.verify_required() )
            if python_version() == 2:
                return self.byteify(response.json())
            else:
                return response.json()
        except requests.exceptions.Timeout:
            return {"success":False,"err":{"code":"TIMEOUT","internal_id":"TIMEOUT_ERROR","msg":"","error_data":[]}}            
        except ValueError:
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
        if self.parse_url(self.api_base_url).scheme == "http":
            return False
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
        qs = self.get_query_string_with_base_params(endpoint, request_params)
        try:
            response = requests.get(self.api_base_url + qs, timeout=self.timeout)
            if python_version() == 2:
                return self.byteify(response.json())
            else:
                return response.json()    
        except requests.exceptions.Timeout:
            return {"success":False,"err":{"code":"TIMEOUT","internal_id":"TIMEOUT_ERROR","msg":"","error_data":[]}}           
        except ValueError:
            return {"success":False,"err":{"code":"SOMETHING_WENT_WRONG","internal_id":"SDK(SOMETHING_WENT_WRONG)","msg":"","error_data":[]}}           


        
    # Byteify encodes input to utf-8 encoding
    # * Author: Mayur
    # * Date: 04/12/2018
    # * Reviewed By:
    #
    # @return same as input
    #       
    def byteify(self, input):
        if isinstance(input, dict):
            return {self.byteify(key): self.byteify(value)
                    for key, value in input.iteritems()}
        elif isinstance(input, list):
            return [self.byteify(element) for element in input]
        elif isinstance(input, unicode):
            return input.encode('utf-8')
        else:
            return input

    #    
    # Generates query string with base params in it
    # 
    # * Author: Mayur
    # * Date: 19/11/2018
    # * Reviewed By:
    #
    # @return string 
    # 
    def get_query_string_with_base_params(self, endpoint, request_params):
        request_timestamp = int(time.time())
        request_params.update({"request_timestamp": request_timestamp, "api_key": self.api_key})
        request_params_str = self.dict_to_urlencoded(request_params)
        string_to_sign = endpoint + "?" + request_params_str
        signature = self.generate_signature(string_to_sign)
        return string_to_sign + "&signature=" + signature




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
        res = None
        if  isinstance(od, dict):
            res = collections.OrderedDict()
            for k, v in sorted(od.items()):
                    res[k] = self.sort_dict(v)
        elif isinstance(od, list):
            res = []
            for val in (od):
                res.append(self.sort_dict(val))      
        else:
            res = od
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
        DEBUG = os.environ.get('OST_KYC_SDK_DEBUG')
        api_secret = api_secret.encode('utf-8') if api_secret else  self.api_secret.encode('utf-8') 
        string_to_sign = self.multisub(string_to_sign)
        if DEBUG:
            print (string_to_sign)
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


       #    
    # Return function compatible with both Python 2 and Python 3
    # 
    # * Author: Mayur
    # * Date: 22/11/2018
    # * Reviewed By:
    #
    # @return function
    # 
    def urlparse(self):
        if python_version() == 2:
            import urlparse
            self.parse_url = urlparse.urlparse
        else:
            self.parse_url = urllib.parse.urlparse

    # Simultaneously perform all substitutions on the subject string.
    # 
    # * Author: Mayur
    # * Date: 22/11/2018
    # * Reviewed By:
    #
    # @return str
    # 
    def multisub(self, subject):
        # tuple[1] is expected value for character tuple[0]
        subs = [('~', '%7E')]
        pattern = '|'.join('(%s)' % re.escape(p) for p, s in subs)
        substs = [s for p, s in subs]
        replace = lambda m: substs[m.lastindex - 1]
        return re.sub(pattern, replace, subject)        

