from random import choice

def get_number_of_posts(max_posts_per_user):
    
    data = []
    
    for i in range(max_posts_per_user + 1):
        if i != 0:
            data.append(i)
            
    number_of_posts = choice(data)
    
    return number_of_posts
    


