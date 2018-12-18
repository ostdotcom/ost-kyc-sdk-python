## OST KYC Python SDK

The official [OST KYC SDK](https://dev.ost.com/docs/kyc/index.html).

## Requirements

To use this node module, developers will need to:
1. Login on [https://kyc.ost.com/admin/login](https://kyc.ost.com/admin/login).
2. Obtain an API Key and API Secret from [https://kyc.ost.com/admin/settings/developer-integrations](https://kyc.ost.com/admin/settings/developer-integrations).

## Documentation

[https://dev.ost.com/docs/kyc](https://dev.ost.com/docs/kyc/index.html)

## Installation

Install OST KYC Python SDK

```bash
> pip install ost_kyc_sdk_python
```

## Example Usage

Require the SDK:

```python
import ost_kyc_sdk_python
```

Initialize the SDK object:

```python
// the latest valid API endpoint is "https://kyc.sandboxost.com", this may change in the future
kyc_sdk = ost_kyc_sdk_python.Services({'api_key': <api_key>, 'api_secret': <api_secret>, 'api_base_url': <api_secret>, 
'config': {'timeout': <desired_timeout_in_secs> }})

Here timeout for requests can be passed inside config, timeout is in seconds (default is 15 secs). 
```

### Users Module 

```python
users_service = kyc_sdk.services.users
```

Create a new user:

```python
r = users_service.create({'email': 'alice+1@ost.com'})
print (r)
```

Get an existing user:

```python
r = users_service.get({'id': '11003'})
print (r)
```

Get a list of users and other data:

```python
r = users_service.list()
print (r)
```

### Users KYC module 

```python
users_kyc_service = kyc_sdk.services.users_kyc
```

Submit KYC:

```python
r = users_kyc_service.submit_kyc({'user_id': 11035, 'first_name':'aniket','last_name':'ayachit', 'birthdate':'21/12/1991', 'country':'india', 'nationality':'indian', 'document_id_number':'arqpa7659a','document_id_file_path':'2/i/016be96da275031de2787b57c99f1471', 'selfie_file_path':'2/i/9e8d3a5a7a58f0f1be50b7876521aebc', 'residence_proof_file_path':'2/i/4ed790b2d525f4c7b30fbff5cb7bbbdb', 'ethereum_address': '0xdfbc84ccac430f2c0455c437adf417095d7ad68e', 'estimated_participation_amount':'2', 'street_address':'afawfveav ','city':'afawfveav', 'state':'afawfveav','postal_code':'afawfveav','investor_proof_files_path':['2/i/9ff6374909897ca507ba3077ee8587da', '2/i/4872730399670c6d554ab3821d63ebce']})
print (r)
```

List Users KYC:

```python
r = users_kyc_service.list()
print (r)
```

Get Users KYC

```python
r = users_kyc_service.get({'user_id':11003})
print (r)
```

Get PUT Presigned url

```python
r = users_kyc_service.get_pre_signed_url_put ({'files': {
    'residence_proof': 'application/pdf',
    'investor_proof_file1': 'application/pdf',
    'investor_proof_file2': 'application/pdf',
    'document_id': 'image/jpeg',
    'selfie': 'image/jpeg'
}})
print (r)
```

Get POST Presigned url

```python
r = users_kyc_service.get_pre_signed_url_post ({'files': {
    'residence_proof': 'application/pdf',
    'investor_proof_file1': 'application/pdf',
    'investor_proof_file2': 'application/pdf',
    'document_id': 'image/jpeg',
    'selfie': 'image/jpeg'
}})
print (r)
```

Send KYC approve email

```python
r = self.users_kyc_service.email_approve({'user_id': 11003})
print (r)

```


Send KYC deny email

```python
r = self.users_kyc_service.email_deny({'user_id': 11003})
print (r)

```

Send KYC report issue email

```python
r = self.users_kyc_service.email_report_issue({'user_id': 11003})
print (r)

```



### Users KYC details Module 

```python
users_kyc_details_service = kyc_sdk.services.users_kyc_details
```

Get user's kyc details

```python
r = users_kyc_details_service.get({'user_id':11003})
print (r)
```

### Validation Module 
    
```python
validator_service = kyc_sdk.services.validators
```

Verify ethereum address

```python
 r = validator_service.verify_ethereum_address({'ethereum_address': '0x32be343b94f860124dc4fee278fdcbd38c102d88'})
 print (r)
 
 ```

 Note: If user want to use non english characters in Python 2, write ```# -*- coding: utf-8 -*- ``` at the beginning of the file.