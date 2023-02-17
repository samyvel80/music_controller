import json

import requests
from identity import *


username = USERNAME
password = PASSWORD

# get Token API URL: POST http://127.0.0.1:8000/api/token/
# BODY : username et password

def getToken_init(username, password):
    url = "http://127.0.0.1:8000/api/token/"
    data = {
        "username": username,
        "password": password
    }
    res = requests.post(url, data= data)
    tokensjsan = res.text
    tokenObject= json.loads(tokensjsan)
    return tokenObject
def getUserList(tokenAccess):
    url = "http://127.0.0.1:8000/product/user-list/"
    headers = {
        "Authorization": "Bearer " + tokenAccess
    }
    res = requests.get(url, headers=headers)

    userlist = res.json()

    return userlist



tokens = getToken_init(username,password)
tokenAccess = tokens["access"]

print("Token Access",tokenAccess)
userlist = getUserList(tokenAccess)
print(userlist)
print("e")



