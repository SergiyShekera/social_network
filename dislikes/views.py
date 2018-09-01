from . import services
from posts.models import Post
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class dislike(APIView):

    def post(self, request, id):

        p = Post.objects.all()
        post = get_object_or_404(p, id=id)
        obj = post
        services.add_dislike(obj, request.user)

        return Response({'status': 'dislike added is successfully'})

class undislike(APIView):

    def post(self, request, id):

        p = Post.objects.all()
        post = get_object_or_404(p, id=id)
        obj = post
        services.remove_dislike(obj, request.user)

        return Response({'status': 'undislike is successfully'})


