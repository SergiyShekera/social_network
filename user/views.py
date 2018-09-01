from .models import User_Acc
from django.contrib.auth.models import User
from .serializers import User_Create_Acc_Serializer
from .serializers import User_Acc_Serializer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response



class User_Acc_Create(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):

        User_data = User_Create_Acc_Serializer(data=request.data)

        if User_data.is_valid():

            username = request.data['username']
            password = request.data['password']
            user = User.objects.create_user(username = username, password = password)

            User_Ac = User_Acc()
            User_Ac.user = user
            User_Ac.first_name = request.data['first_name']
            User_Ac.last_name = request.data['last_name']
            User_Ac.save()

            return Response({'status': 'Add'})

        else:
            return Response({'status': 'Error'})


class User_lists(APIView):

    def get(self, request):

        users  = User_Acc.objects.all()
        serializer = User_Acc_Serializer(users, many=True)

        return Response({'data': serializer.data})
