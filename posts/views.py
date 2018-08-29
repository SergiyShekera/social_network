from .models import Post
from rest_framework import permissions
from .serializers import Post_Serializer
from .serializers import Post_Create_Serializer


from rest_framework.views import APIView
from rest_framework.response import Response



class Posts_lists(APIView):

    def get(self, request):

        posts  = Post.objects.all()

        serializer = Post_Serializer(posts, many=True)
        return Response({'data': serializer.data})


class Posts_Create(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        post = Post_Create_Serializer(data=request.data)

        if post.is_valid():
            post.save(creater=request.user)
            return Response({'status': 'Add'})

        else:
            return Response({'status': 'Error'})

