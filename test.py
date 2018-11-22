from ost_kyc_sdk.services import Services
from config import Config
from ost_kyc_sdk.util.http_helper import HTTPHelper
import time
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