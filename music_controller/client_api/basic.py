import requests


#viewset_endpoint = 'http://127.0.0.1:8000/product/'
endpoint = 'http://127.0.0.1:8000/product/'
#endpoint = 'http://httpbin.org/anything'
res = requests.post(endpoint, json={'name': 'pasteque', 'content': 'just pasteque','price':20})
print(res.json())
print(res.status_code)
