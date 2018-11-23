import os
class Config:
    API_KEY = os.environ['API_KEY']
    API_SECRET = os.environ['API_SECRET']
    API_BASE_URL =  os.environ['API_BASE_URL']
    test_obj_for_signature = { 
                'k1':'Rachin',
               'k2':'tejas', 
               'list2':[
                    {'a':'L21A', 'b':'L21B'}, 
                    {'a':'L22A', 'b':'L22B'}, 
                    {'a':'L23A', 'b':'L23B'}
                ],
                'make_mistakes': None,
                'nice_param': [],
                'empty_obj': {},
                'empty_str': '',
                'garbage_str': "~^[]%$#@!&*~,./?~()-_'this is garbage",
                'id':11003,
                'email': 'mayur+67@ost.com'
                }
    test_obj_for_requests = {
                'garbage_str': "~^[]%$#@!&*~,./?~()-_'this is garbage",
                'id':11003,
                'email': 'mayur+67@ost.com'
    }                
    test_endpoint = '/api/v2/users'            
    GENERATED_SIGNATURE = "c42188c53bfdf84e542a0a9c0a78d19c9f497c61e816f169e1907bc98477eb82"

