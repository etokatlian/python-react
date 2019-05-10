from posts.models import Post, Author
from posts.serializers import PostSerializer, AuthorSerializer
from rest_framework import generics


class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
