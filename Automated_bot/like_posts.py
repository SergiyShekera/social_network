import requests
from get_JWT import get_JWT

def like_posts(data_user, post_id):
    
    url = f'http://localhost:8080/likes/like/{post_id}'
    
    username = data_user['username']
    password = data_user['password']
    
    JWT = get_JWT(username, password)   
    header = {"Authorization" : JWT}

    data = {'name': 'some',
            'text': 'qewqe1wq'}
    
    try:
        res = requests.post(url, headers=header)
        i = res.json()
        print(f'Post with id={post_id} liked successfully')
            
    except:
        print('Could not liked post')




