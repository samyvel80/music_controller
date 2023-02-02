import requests


#viewset_endpoint = 'http://127.0.0.1:8000/product/1/detail'
endpoint = 'http://127.0.0.1:8000/product/2/detail'
#endpoint = 'http://httpbin.org/anything'
res = requests.get(endpoint)
print(res.json())
print(res.status_code)