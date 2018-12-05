import os 
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()  

setup(name='ost_kyc_sdk_python',    
      version = '2.0.0',
      description = 'OST KYC SDK in python',
      long_description = read('README.md'),
      long_description_content_type='text/markdown',
      url='https://github.com/OpenSTFoundation/ost-kyc-sdk-python',
      packages = find_packages(),
      install_requires = ['requests'],
      license = "MIT",
      zip_safe = False  
)