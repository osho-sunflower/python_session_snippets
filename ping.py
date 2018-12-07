import requests

request = requests.get('https://api.brivity-staging.com')
print(f'Status Code: {request.status_code}')
print('Headers:')
for header, value in request.headers.items():
	print(f'\t{header}: {value}')
print(f'Encoding: {request.encoding}')