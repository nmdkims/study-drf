from rest_framework import serializers
from .models import homework_message

class homework_messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = homework_message
        fields = 'message'
