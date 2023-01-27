import requests


#viewset_endpoint = 'http://127.0.0.1:8000/product/'
endpoint = 'http://127.0.0.1:8000/product/1/'
#endpoint = 'http://httpbin.org/anything'
res = requests.get(endpoint)
print(res.json())
print(res.status_code)