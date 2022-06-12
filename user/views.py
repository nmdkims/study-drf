from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .serializers import UserSerializer
from blog.models import Article
from .models import Hobby

# Create your views here.

class MyAwesomePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated) or bool(user and user.is_staff)
        return result


class UserApiView(APIView):
    permission_classes = [permissions.AllowAny]  # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능
    # permission_classes = [MyAwesomePermission]
    serializer_class = UserSerializer


    def get(self, request):
        queryset = list(Article.objects.filter(writer=self.request.user).values())
        # user = request.user
        # queryset.append(user)
        # try:
        #     hobby = Hobby.objects.get(username=user)
        # except Hobby.DoesNotExist:
        #
        #     return Response({'error': '오브젝트가 존재하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(queryset)

        # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)


    # def put(self, request):
    #     return Response({'message': 'put method!!'})
    #
    # def delete(self, request):
    #     return Response({'message': 'delete method!!'})
