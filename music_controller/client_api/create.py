import requests

endpoint = 'http://127.0.0.1:8000/product/create-list/'
#endpoint = 'http://httpbin.org/anything'
res = requests.post(endpoint, json={'name': 'car', 'content': 'just','price':1100})
print(res.json())
print(res.status_code)