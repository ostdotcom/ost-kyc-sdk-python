import re
from ..util.http_helper import HTTPHelper
class Base:
    def __init__(self, params):
        self.http_helper = HTTPHelper(params)

    # 
    # Raises exception if given parameter is not present in dict
    # * Author: Mayur
    # * Date: 19/11/2018
    # * Reviewed By:
    #
    # Raise Exception
    #   
    def raise_exception_if_param_absent_or_invalid(self, params, parameter):
        param = params.get(parameter) 
        if  type(param) == str:
            param = param.strip()          
        if (not param and not str(param) == '0'): 
            raise Exception("missing "+ parameter)
        is_matched = re.match("^[a-z\d\-\.]+$", str(param), re.IGNORECASE )
        if not is_matched:     
            raise Exception("invalid "+ parameter)     




    # 
    # Delete given key from dict
    # * Author: Mayur
    # * Date: 19/11/2018
    # * Reviewed By:
    #
    # Return None
    #  
    def delete_key_from_params(self, params, parameter):
        if parameter in params:
            del params[parameter]







