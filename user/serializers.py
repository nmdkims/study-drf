# from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from user.models import User
from blog.serializers import commentSerializer


class UserSerializer(serializers.ModelSerializer):
    comment = commentSerializer()

    class Meta:
        model = User
        # fields = "__all__"
        fields = ['username', 'password', 'comment']
