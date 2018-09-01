from django.urls import path
from dislikes.views import dislike
from dislikes.views import undislike


app_name='dislikes'

urlpatterns = [
    path('dislike/<int:id>', dislike.as_view()),
    path('undislike/<int:id>', undislike.as_view())
]
