from django.urls import path
from posts.views import Posts_lists, Posts_Create

app_name='posts'

urlpatterns = [
    path('api/posts-list', Posts_lists.as_view()),
    path('api/posts-create', Posts_Create.as_view()),
    # path('api/user', User_View.as_view()),

]
