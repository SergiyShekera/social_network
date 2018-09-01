from django.urls import path
from likes.views import like
from likes.views import unlike


app_name='likes'

urlpatterns = [
    path('like/<int:id>', like.as_view()),
    path('unlike/<int:id>', unlike.as_view())
]
