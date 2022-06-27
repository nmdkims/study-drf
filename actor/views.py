# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from actor.serializers import actorSerializer

class MyAwesomePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated) or bool(user and user.is_staff)
        return result


class ActorView(APIView):  # CBV 방식
    # permission_classes = [permissions.AllowAny]  # 누구나 view 조회 가능

    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    permission_classes = [MyAwesomePermission]  # 로그인 된 사용자만 view 조회 가능
    # serializer_class = actorSerializer

    def get(self, request):
        return Response(actorSerializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({'message': 'post method!!'})

    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})
