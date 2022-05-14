from rest_framework import serializers
from .models import BlogPost



class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ['id','Author', 'Title', 'Body', 'Created_At','Updated_At']

class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ['id','Author', 'Title', 'Body', 'Created_At','Updated_At']