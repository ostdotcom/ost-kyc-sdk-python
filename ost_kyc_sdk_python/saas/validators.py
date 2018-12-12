from .base import Base
class Validators(Base):
    def __init__(self, params):
        Base.__init__(self, params)

    # 
    # Verify Ethereum address
    # * Author: Mayur
    # * Date: 20/11/2018
    # * Reviewed By:
    #
    # Return dict
    #  
    def verify_ethereum_address(self, params):
        endpoint = "/api/v2/ethereum-address-validation"
        return self.http_helper.send_get_request(endpoint, params)

        