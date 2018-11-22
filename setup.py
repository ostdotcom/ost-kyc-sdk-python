from setuptools import setup, find_packages
setup(name='ost_kyc_sdk',    
      version='2.0.0',
      description='OST KYC SDK in python',
      url='https://github.com/OpenSTFoundation/kyc-sdk-python',
      packages = find_packages(),
      install_requires = ['requests'],
      zip_safe=False  
)