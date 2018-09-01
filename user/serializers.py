from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User_Acc


class User_Serializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class User_Acc_Serializer(serializers.ModelSerializer):

    user = User_Serializer()

    class Meta:

        model = User_Acc
        fields = ('user', 'first_name', 'last_name')


class User_Create_Acc_Serializer(serializers.Serializer):

    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)

    class Meta:

        fields = ('username', 'password', 'first_name', 'last_name')
