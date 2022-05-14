from rest_framework import generics
from .models import BlogPost
from .serializers import PostSerializer,PostCreateSerializer


class PostList(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer

class PostUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer

class PostCreate(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostCreateSerializer