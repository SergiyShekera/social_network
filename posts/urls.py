from django.urls import path
from posts.views import Posts_lists
from posts.views import Posts_Create
from posts.views import Post_Detail_View



app_name='posts'

urlpatterns = [
    path('api/posts-list', Posts_lists.as_view()),
    path('api/posts-create', Posts_Create.as_view()),
    path('api/post-detail/<int:id>/', Post_Detail_View.as_view()),

]
