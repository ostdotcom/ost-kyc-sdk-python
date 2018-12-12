
from .base import Base

class Users(Base):
    def __init__(self, params):
        Base.__init__(self, params)
        self.endpoint = '/api/v2/users'

    # 
    # Create user 
    # * Author: Mayur
    # * Date: 20/11/2018
    # * Reviewed By:
    #
    # Return dict
    # 
    def create(self, params):
        return self.http_helper.send_post_request(self.endpoint , params)

    # 
    # Get user info
    # * Author: Mayur
    # * Date: 20/11/2018
    # * Reviewed By:
    #
    # Return dict
    # 
    def get(self, params={}):
        self.raise_exception_if_param_absent_or_invalid(params, 'id')
        endpoint =  self.endpoint + "/" + str(params.get('id'))
        self.delete_key_from_params(params, 'id')   
        return self.http_helper.send_get_request(endpoint, params)

    # 
    # List user info
    # * Author: Mayur
    # * Date: 20/11/2018
    # * Reviewed By:
    #
    # Return dict
    # 
    def list(self, params={}):
        return self.http_helper.send_get_request(self.endpoint, params)



