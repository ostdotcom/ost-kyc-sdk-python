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
    def raise_exception_if_param_absent(self, params, parameter):
        param = params.get(parameter).strip() if type(params.get(parameter)) == str else params.get(parameter)
        if not params.get(parameter) and not str(param) == '0': 
            raise Exception("missing "+ parameter)



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







