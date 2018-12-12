from .base import Base
class UsersKYCDetails(Base):
    
    def __init__(self, params):
        Base.__init__(self, params)
        self.endpoint = "/api/v2/users-kyc-detail"

    # 
    # Get user KYC details for given user_id
    # * Author: Mayur
    # * Date: 20/11/2018
    # * Reviewed By:
    #
    # Return dict
    #          
    def get(self, params):
        self.raise_exception_if_param_absent_or_invalid(params, 'user_id')
        endpoint =  self.endpoint + "/" + str(params.get('user_id'))
        self.delete_key_from_params(params, 'user_id')   
        return self.http_helper.send_get_request(endpoint, params)  


