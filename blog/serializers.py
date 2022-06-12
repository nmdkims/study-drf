from rest_framework import serializers
from .models import Article, Category

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