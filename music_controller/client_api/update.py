import requests

endpoint = 'http://127.0.0.1:8000/product/10/update'
#endpoint = 'http://httpbin.org/anything'
res = requests.put(endpoint, json={'name': 'orange300', 'content': '', 'price': 100})
print(res.json())
print(res.status_code)