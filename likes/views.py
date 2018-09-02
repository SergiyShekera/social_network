from . import services
from posts.models import Post
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class like(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):

        p = Post.objects.all()
        post = get_object_or_404(p, id=id)
        obj = post
        services.add_like(obj, request.user)

        return Response({'status': 'like added is successfully'})

class unlike(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):

        p = Post.objects.all()
        post = get_object_or_404(p, id=id)
        obj = post
        services.remove_like(obj, request.user)

        return Response({'status': 'unlike is successfully'})


