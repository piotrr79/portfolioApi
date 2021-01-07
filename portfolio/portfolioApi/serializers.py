from rest_framework import serializers
from .models import Blog, Category, Article

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name', 'category_reference')
        
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        # @ToDo - get category from Category Serializer rahter than from 'depth'
        depth = 1
        fields = ('title', 'category', 'lead', 'content', 'link_url', 'photo', 'published', 'created')
        
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'slug', 'content')