from ost_kyc_sdk.services import Services
from config import Config
from ost_kyc_sdk.util.http_helper import HTTPHelper
import time


# kyc_sdk.services.users_kyc.get_pre_signed_url_put ({'files': {
#        'residence_proof': 'application/pdf',
#        'investor_proof_file1': 'application/pdf',
#        'investor_proof_file2': 'application/pdf',
#        'document_id': 'image/jpeg',
#        'selfie': 'image/jpeg'
#     }})

# r = kyc_sdk.services.users.create(
#       Config.test_obj
# )
#r = kyc_sdk.services.users_kyc_details.get({'user_id': 11003})


# test_params = {'k1':'Rachin',
#                'k2':'tejas', 
#                'list2':[
#                     {'a':'L21A', 'b':'L21B'}, 
#                     {'a':'L22A', 'b':'L22B'}, 
#                     {'a':'L23A', 'b':'L23B'}
#                 ]
#              }

#r = kyc_sdk.services.users.get(Config.test_obj)
# r = kyc_sdk.services.users.get({'l':"", 'id':"11003",'id1': None, 'id3': [], 'id4': [''], 'id5': [None],
# 'id6': {}, 'id7': {'id1': None}, 'id8': {'id': [], 'ooo': '1', 'ii': '?><:"{}|+_)(*&^%$#@!~1`234567890-=[]\;,./'}})

# kyc_sdk.services.users.list()    
# r = kyc_sdk.services.users_kyc.submit_kyc(
#     params = {'user_id': 11035, 'first_name':'aniket','last_name':'ayachit', 'birthdate':'21/12/1991', 'country':'india', 'nationality':'indian', 'document_id_number':'arqpa7659a','document_id_file_path':'2/i/016be96da275031de2787b57c99f1471', 'selfie_file_path':'2/i/9e8d3a5a7a58f0f1be50b7876521aebc', 'residence_proof_file_path':'2/i/4ed790b2d525f4c7b30fbff5cb7bbbdb', 'ethereum_address': '0xdfbc84ccac430f2c0455c437adf417095d7ad68e', 'estimated_participation_amount':'2', 'street_address':'afawfveav ','city':'afawfveav', 'state':'afawfveav','postal_code':'afawfveav','investor_proof_files_path':['2/i/9ff6374909897ca507ba3077ee8587da', '2/i/4872730399670c6d554ab3821d63ebce']}
#     )
# kyc_sdk.services.users_kyc.get({'user_id': 11003})
#kyc_sdk.services.users_kyc.list()


# kyc_sdk.services.users_kyc.get_pre_signed_url_post ({'files': {
#        'residence_proof': 'application/pdf',
#        'investor_proof_file1': 'application/pdf',
#        'investor_proof_file2': 'application/pdf',
#        'document_id': 'image/jpeg',
#        'selfie': 'image/jpeg'
#     }})


# kyc_sdk.services.users_kyc.get_pre_signed_url_put ({'files': {
#        'residence_proof': 'application/pdf',
#        'investor_proof_file1': 'application/pdf',
#        'investor_proof_file2': 'application/pdf',
#        'document_id': 'image/jpeg',
#        'selfie': 'image/jpeg'
#     }})

#kyc_sdk.services.validators.verify_ethereum_address({'ethereum_address':"0x81b7e08f65bdf5648606c89998a9cc8164397647"})    

#print (r)


import unittest

class TestStringMethods(unittest.TestCase):

    kyc_sdk = Services({'api_key': Config.API_KEY, 'api_secret': Config.API_SECRET, 'api_base_url': Config.API_BASE_URL})
    def test_signature(self):
        http_helper_obj = HTTPHelper({})
        generated_signature = http_helper_obj.get_signature_for_test(Config.test_obj_for_signature, Config.test_endpoint, Config.API_SECRET)    
        self.assertEqual(Config.GENERATED_SIGNATURE, generated_signature)

    def test_post_request(self):
        test_obj = Config.test_obj_for_requests
        test_obj.update(email='testuser+'+ str(int(time.time())) +'@ost.com')
        r = self.kyc_sdk.services.users.create(
            test_obj
        )
        self.assertEqual(r['success'], True)
       
    def test_get_request(self):
        r = self.kyc_sdk.services.users.list()
        self.assertEqual(r['success'], True)
        

if __name__ == '__main__':
    unittest.main()