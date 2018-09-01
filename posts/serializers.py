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

        model = Post
        fields = ('id', 'creater', 'name', 'text', 'date', 'total_likes', 'total_dislikes')


class Post_Create_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('name', 'text')
