from rest_framework.views import APIView
from rest_framework.response import Response

from base.api.serializers import PostSerializer
from posts.models import Post


class home(APIView):

    def get(self, request):

        routes = [
            "/api/posts/",
            "/api/token/",
            "/api/token/refresh/",
        ]
        return Response(routes)


class PostList(APIView):

    def get(self, request):

        posts = Post.objects.all()

        post_serializer = PostSerializer(posts, many=True)

        return Response(post_serializer.data)

    def post(self, request):

        post_serializer = PostSerializer(data=request.data)

        if post_serializer.is_valid():
            post_serializer.save()

            return Response(post_serializer.data, status=201)

        return Response(post_serializer.errors, status=400)
