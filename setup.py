import os 
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()  

setup(name='ost_kyc_sdk_python',    
      version = '2.0.0b',
      description = 'OST KYC SDK in python',
      long_description = read('README.md'),
      url='https://github.com/OpenSTFoundation/kyc-sdk-python',
      packages = find_packages(),
      install_requires = ['requests'],
      license = "MIT",
      zip_safe = False  
)