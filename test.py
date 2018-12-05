# -*- coding: utf-8 -*-
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

    # def test_create_new_user(self):
    #     test_obj = Config.test_obj_for_requests
    #     test_obj.update(email='testuser+'+ str(int(time.time())) + '_' + full_python_version() +'@ost.com')
    #     r = self.users_service.create(
    #         test_obj
    #     )
    #     DEBUG = os.environ.get('OST_KYC_SDK_DEBUG')
    #     if DEBUG:
    #         print (r)
    #     self.assertEqual(r['success'], True, "Create new user failed")

    # def test_get_user(self):     
    #     r = self.users_service.get({'id': '11550'})
    #     print (r)
        # self.assertEqual(r['success'], True, "Get user is failed")

    # def test_get_user_list(self):
    #     r = self.users_service.list()
    #     self.assertEqual(r['success'], True, "Get users list is failed")

    def test_submit_kyc(self):
        pass
       # r = self.users_kyc_service.submit_kyc({'user_id':'11550','first_name':'日本人の',  'last_name':'日本人の氏名',  'birthdate':'29/07/1992', 'country':'india', 'nationality':'indian', 'document_id_number':'dmdps9634c', 'document_id_file_path':'7/d/00f67882ba447f704b75d7a5702e6572', 'selfie_file_path':'7/i/006c6351efad152ecdf5b175bb6d6fb0', 'ethereum_address':'0xEC305b4c269dEd899b6fBA12776fbbDBdC564793', 'estimated_participation_amount':'1', 'street_address':'pune', 'city':'pune', 'state':'maharashtra', 'postal_code':'41036'})
       # print (r)
        # self.assertEqual(r['success'], False, "Submit KYC is failed")

    # def test_get_users_kyc_list(self):
    #     r = self.users_kyc_service.list()
    #     self.assertEqual(r['success'], True, "get users KYC list is failed")

    # def test_get_users_kyc(self):
    #     r = self.users_kyc_service.get({'user_id':11550})
    #     print (r)
        #self.assertEqual(r['success'], True, "get users KYC is failed")

    # def test_get_presigned_url_put(self):
    #     r = self.users_kyc_service.get_pre_signed_url_put (self.get_presigned_url_obj)
    #     self.assertEqual(r['success'], True, "get presigned url for PUT is failed")

    # def test_get_pre_signed_url_post(self):
    #     r = self.users_kyc_service.get_pre_signed_url_put (self.get_presigned_url_obj)
    #     self.assertEqual(r['success'], True, "get presigned url for PUT is failed")   

    def test_get_users_kyc_details(self):
        
        r = self.users_kyc_details_service.get({'user_id':11550})
        print (r['data']['user_kyc']['first_name'])
        r = self.users_kyc_service.submit_kyc({'user_id':'11550','first_name':r['data']['user_kyc']['first_name'],  'last_name':'日',  'birthdate':'29/07/1992', 'country':'india', 'nationality':'indian', 'document_id_number':'dmdps9634c', 'document_id_file_path':'7/d/00f67882ba447f704b75d7a5702e6572', 'selfie_file_path':'7/i/006c6351efad152ecdf5b175bb6d6fb0', 'ethereum_address':'0xEC305b4c269dEd899b6fBA12776fbbDBdC564793', 'estimated_participation_amount':'1', 'street_address':'pune', 'city':'pune', 'state':'maharashtra', 'postal_code':'41036'});
        print (r)
        

    # def test_validate_eth_address(self):
    #     r = self.validator_service.verify_ethereum_address({'ethereum_address': '0x32be343b94f860124dc4fee278fdcbd38c102d88'})
    #     self.assertEqual(r['success'], True, "Ethereum address is correct")

    # def test_signature(self):
    #     http_helper_obj = HTTPHelper({})
    #     generated_signature = http_helper_obj.get_signature_for_test(Config.test_obj_for_signature, Config.test_endpoint, Config.API_SECRET_TO_TEST_SIGNATURE)    
    #     self.assertEqual(Config.GENERATED_SIGNATURE, generated_signature, 'Generated signature and given signature should be matched')

if __name__ == '__main__':
    unittest.main()
    