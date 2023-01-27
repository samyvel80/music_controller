import requests

endpoint = 'http://127.0.0.1:8000/product/create/'
#endpoint = 'http://httpbin.org/anything'
res = requests.post(endpoint, json={'name': 'kiwi', 'content': 'just','price':10})
print(res.json())
print(res.status_code)