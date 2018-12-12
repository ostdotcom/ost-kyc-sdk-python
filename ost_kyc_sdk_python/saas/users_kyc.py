from .base import Base
class UsersKYC(Base):
    def __init__(self, params):
        Base.__init__(self, params)
        self.endpoint = '/api/v2/users-kyc'

    # 
    # Submit KYC 
    # * Author: Mayur
    # * Date: 20/11/2018
    # * Reviewed By:
    #
    # Return dict
    #      
    def submit_kyc(self, params):
        self.raise_exception_if_param_absent_or_invalid(params, 'user_id')
        endpoint =  self.endpoint + "/" + str(params.get('user_id'))
        self.delete_key_from_params(params, 'user_id')
        return self.http_helper.send_post_request(endpoint, params)

    # 
    # get user's KYC information, in params user_id is mandatory parameter
    # * Author: Mayur
    # * Date: 20/11/2018
    # * Reviewed By:
    #
    # Return dict
    # 
    def get(self, params={}):
        self.raise_exception_if_param_absent_or_invalid(params, 'user_id')
        endpoint =  self.endpoint + "/" + str(params.get('user_id'))
        self.delete_key_from_params(params, 'user_id')   
        return self.http_helper.send_get_request(endpoint, params)  


    # 
    # Return list of user's KYC information 
    # * Author: Mayur
    # * Date: 20/11/2018
    # * Reviewed By:
    #
    # Return dict
    # 
    def list(self, params={}):
        return self.http_helper.send_get_request(self.endpoint, params)

    # 
    # Get presigned url for PUT request
    # * Author: Mayur
    # * Date: 20/11/2018
    # * Reviewed By:
    #
    # Return dict
    # 
    def get_pre_signed_url_put(self, params):
        suffix = "/pre-signed-urls/for-put"
        return self.http_helper.send_get_request(self.endpoint + suffix, params)
        
    # 
    # Get presigned url for POST request
    # * Author: Mayur
    # * Date: 20/11/2018
    # * Reviewed By:
    #
    # Return dict
    # 
    def get_pre_signed_url_post(self, params):
        suffix = "/pre-signed-urls/for-post"
        return self.http_helper.send_get_request(self.endpoint + suffix, params)
        
