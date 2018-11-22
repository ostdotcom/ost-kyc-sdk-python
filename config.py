import os
class Config:
    API_KEY = os.environ['API_KEY']
    API_SECRET = os.environ['API_SECRET']
    API_BASE_URL = 'http://kyc.developmentost.com:8080'
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
    GENERATED_SIGNATURE = os.environ['GENERATED_SIGNATURE_FOR_TEST']

