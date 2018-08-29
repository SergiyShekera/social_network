from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post


class User_Serializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')

class Post_Serializer(serializers.ModelSerializer):

    creater = User_Serializer()

    class Meta:
        creater = User_Serializer()
        model = Post
        fields = ('id', 'creater', 'name', 'text')


class Post_Create_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('name', 'text')
