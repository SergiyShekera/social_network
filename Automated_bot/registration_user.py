import requests
import json


def registration_user(user):

    url = 'http://localhost:8080/user/api/registration'
    
    data_user = {'username': user['username'],
                 'password': user['password'],
                 'first_name': user['first_name'],
                 'last_name': user['last_name']}
    
    try:
        
        res = requests.post(url, data=data_user)
        i = res.json()
        
        if i['data']['status'] == 'Add':
            print('User registered successfully')
            return data_user
        
        else:
            print('Could not register user')
        
    except:
        print('Could not register user')
            
