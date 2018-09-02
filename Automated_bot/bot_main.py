import requests
import json
from create_post import create_post
from get_JWT import get_JWT
from like_posts import like_posts
from registration_user import registration_user
from get_random_id import get_random_id
from get_all_posts_id import get_all_posts_id
from get_number_of_posts import get_number_of_posts
from config import number_of_users
from config import max_posts_per_user
from config import max_likes_per_use
from users import users



def run_bot(user, number_of_posts, max_likes_per_use):
    
    data_user = registration_user(user)

    posts_id = get_all_posts_id()

    while number_of_posts != 0:
        
        create_post(data_user)
        number_of_posts -= 1

    print('All posts created')

    while max_likes_per_use != 0:
        
        post_id = get_random_id(posts_id)      
        like_posts(data_user, post_id)
        max_likes_per_use -= 1

    print('All likes is added')


    
if __name__ == '__main__':

    print('number_of_users = ' + str(number_of_users))
    
    while number_of_users !=0:

        i = number_of_users
        
        user = users[f'user_{i}']
        
        print(user)
        
        number_of_posts = get_number_of_posts(max_posts_per_user)
        
        run_bot(user, number_of_posts, max_likes_per_use)
        
        number_of_users -= 1

    print('-----' * 5)
    print('The bot has successfully completed the work')
    print('-----' * 5)
    
    q = input('press Enter to exit')















