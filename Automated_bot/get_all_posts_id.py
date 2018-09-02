import requests
import json


def get_all_posts_id():

    url = 'http://localhost:8080/posts/api/posts-list'
          
    res = requests.get(url)
    data = res.json()
        
    data = data['data']['data']
    posts_id = []
    
    for i in data:
        posts_id.append(i['id'])

    return posts_id
