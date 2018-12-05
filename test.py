import os
import json
import time
import unittest
from config import Config
from ost_kyc_sdk_python.services import Services
from ost_kyc_sdk_python.util.http_helper import HTTPHelper
from ost_kyc_sdk_python.util.python_version import full_python_version

class TestStringMethods(unittest.TestCase):
    kyc_sdk = Services({'api_key': Config.API_KEY, 'api_secret': Config.API_SECRET, 'api_base_url': Config.API_BASE_URL, 
    'config':{'timeout':10   }})
    users_service = kyc_sdk.services.users
    users_kyc_service = kyc_sdk.services.users_kyc
    users_kyc_details_service = kyc_sdk.services.users_kyc_details
    validator_service = kyc_sdk.services.validators
    get_presigned_url_obj = {'files': {
        'residence_proof': 'application/pdf',
        'investor_proof_file1': 'application/pdf',
        'investor_proof_file2': 'application/pdf',
        'document_id': 'image/jpeg',
        'selfie': 'image/jpeg'
        }}

    def test_create_new_user(self):
        test_obj = Config.test_obj_for_requests
        test_obj.update(email='testuser+'+ str(int(time.time())) + '_' + full_python_version() +'@ost.com')
        r = self.users_service.create(
            test_obj
        )
        DEBUG = os.environ.get('OST_KYC_SDK_DEBUG')
        if DEBUG:
            print (r)
        self.assertEqual(r['success'], True, "Create new user failed")

    def test_get_user(self):     
        r = self.users_service.get({'id': Config.USER_ID})
        self.assertEqual(r['success'], True, "Get user is failed")

    def test_get_user_with_id_zero(self):
        r = self.users_service.get({'id': 0})
        self.assertEqual(r['success'], False, "Get user with id 0 failed")

    def test_get_user_with_id_blank(self):
        try:
            r = self.users_service.get({'id': '  '})
            self.fail("test get user with blank is failed")
        except Exception as e:
            self.assertEqual(str(e), 'missing  or invalid id', "test get user with blank is failed") 

    def test_get_user_with_id_invalid(self):
        try:
            r = self.users_service.get({'id': 'BB&#@@#^@&#^@#^'})
            self.fail("test get user with blank is failed")
        except Exception as e:
            self.assertEqual(str(e), 'missing  or invalid id', "test get user with blank is failed")            



    def test_get_user_list(self):
        r = self.users_service.list()
        self.assertEqual(r['success'], True, "Get users list is failed")

    def test_submit_kyc(self):
        r = self.users_kyc_service.submit_kyc({'user_id': 11035, 'first_name':'aniket','last_name':'ayachit', 'birthdate':'21/12/1991', 'country':'india', 'nationality':'indian', 'document_id_number':'arqpa7659a','document_id_file_path':'2/i/016be96da275031de2787b57c99f1471', 'selfie_file_path':'2/i/9e8d3a5a7a58f0f1be50b7876521aebc', 'residence_proof_file_path':'2/i/4ed790b2d525f4c7b30fbff5cb7bbbdb', 'ethereum_address': '0xdfbc84ccac430f2c0455c437adf417095d7ad68e', 'estimated_participation_amount':'2', 'street_address':'afawfveav ','city':'afawfveav', 'state':'afawfveav','postal_code':'afawfveav','investor_proof_files_path':['2/i/9ff6374909897ca507ba3077ee8587da', '2/i/4872730399670c6d554ab3821d63ebce']})
        self.assertEqual(r['success'], False, "Submit KYC is failed")

    def test_get_users_kyc_list(self):
        r = self.users_kyc_service.list()
        self.assertEqual(r['success'], True, "get users KYC list is failed")

    def test_get_users_kyc(self):
        r = self.users_kyc_service.get({'user_id':Config.USER_ID})
        self.assertEqual(r['success'], True, "get users KYC is failed")

    def test_get_presigned_url_put(self):
        r = self.users_kyc_service.get_pre_signed_url_put (self.get_presigned_url_obj)
        self.assertEqual(r['success'], True, "get presigned url for PUT is failed")

    def test_get_pre_signed_url_post(self):
        r = self.users_kyc_service.get_pre_signed_url_put (self.get_presigned_url_obj)
        self.assertEqual(r['success'], True, "get presigned url for PUT is failed")   

    def test_get_users_kyc_details(self):
        r = self.users_kyc_details_service.get({'user_id':Config.USER_ID})
        self.assertEqual(r['success'], True, "get users kyc details failed")

    def test_validate_eth_address(self):
        r = self.validator_service.verify_ethereum_address({'ethereum_address': '0x32be343b94f860124dc4fee278fdcbd38c102d88'})
        self.assertEqual(r['success'], True, "Ethereum address is correct")

    def test_signature(self):
        http_helper_obj = HTTPHelper({})
        generated_signature = http_helper_obj.get_signature_for_test(Config.test_obj_for_signature, Config.test_endpoint, Config.API_SECRET_TO_TEST_SIGNATURE)    
        self.assertEqual(Config.GENERATED_SIGNATURE, generated_signature, 'Generated signature and given signature should be matched')

if __name__ == '__main__':
    unittest.main()
    