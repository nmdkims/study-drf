from rest_framework import serializers
from .models import Article, Category, Comment

class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article

        fields = [
            'writer',
            'title',
            'category',
            'description'
        ]

class articleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'categoryname'

class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment

        fields = [
            'title',
            'writer',
            'created',
            'content'
        ]