import requests
import json
from get_JWT import get_JWT


def create_post(data_user):

    url = 'http://localhost:8080/posts/api/posts-create'
    
    username = data_user['username']
    password = data_user['password']
    
    JWT = get_JWT(username, password)   
    header = {"Authorization" : JWT}

    data = {'name': 'dqweqqqweq',
            'text': 'dwqdqweqwwqwdqewdq'}
    
    try:
        
        
        res = requests.post(url, headers=header, data=data)
        i = res.json()
        
        if i['data']['status'] == 'Add':
                print('Post created successfully')
                
        else:
            print('Could not created post')
            
    except:
        print('Could not created post')
            


