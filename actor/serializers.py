from rest_framework import serializers
from .models import Actor, Category

class actorSerializer(serializers.ModelSerializer):
    voice = serializers.ImageField(use_url=True)

    class Meta:
        model = Actor
        fields = {
            'actorname',
            'writer',
            'category',
            'voice'
        }

class actorCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'categoryname'