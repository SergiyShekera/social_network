import requests
import json


def get_JWT(username, password):

    url = 'http://localhost:8080/auth/jwt/create/'
    
    data = {'username': username,
            'password': password}

    res = requests.post(url, data=data)
    i = res.json()
  
    JWT = i['data']['token']
    JWT = 'JWT ' + JWT
    
    return JWT






