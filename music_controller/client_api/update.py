import requests
from getpass import getpass

enppoint_token ='http://127.0.0.1:8000/api/auth'
username= input("tapez votre login:\n")
password = getpass("Entrer votre password:\n")

auth_res = requests.post(enppoint_token, json = {'username': username, 'password': password})
print(auth_res.json())
token = auth_res.json()
token_str = token['token']
if auth_res.status_code == 200:

    endpointModelViewset = "http://127.0.0.1:8000/product/v2/ProductViewset/2/"

    headers = {
        'Authorization': f'Bearer {token_str}'
       # 'Authorization' : 'Token 087e2c54735a07410c1e36fe34e42aae549fbe07'
    }
    res = requests.put(endpointModelViewset, headers=headers, json={'email': 'ssss@gmail.com', 'name': 'client', 'content': '', 'price': 100})

    print(res.json())
    print(res.status_code)