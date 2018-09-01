from django.urls import path
from user.views import User_Acc_Create
from user.views import User_lists


app_name='user'

urlpatterns = [
    path('api/registration', User_Acc_Create.as_view()),
    path('api/user-list', User_lists.as_view()),
]
