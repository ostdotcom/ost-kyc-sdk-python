from .users import Users
from .users_kyc import UsersKYC
from .users_kyc_details import UsersKYCDetails
from .validators import Validators

class Manifest:

    def __init__(self, params):
        self.users = Users(params)
        self.users_kyc = UsersKYC(params)
        self.users_kyc_details = UsersKYCDetails(params)
        self.validators = Validators(params)
        
