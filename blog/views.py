# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from blog.models import Article
from .serializers import articleSerializer

from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone


class RegistedMoreThanAWeekUser(BasePermission):
    """
    가입일 기준 1주일 이상 지난 사용자만 접근 가능
    """
    message = '가입 후 3일 이상 지난 사용자만 사용하실 수 있습니다.'

    def has_permission(self, request, view):
        if request.method == "GET":
            return True

        return bool(request.user and request.user.join_date < (timezone.now() - timedelta(days=3)))

class MyAwesomePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated) or bool(user and user.is_staff)
        return result


class ArticleView(APIView):  # CBV 방식
    # permission_classes = [permissions.AllowAny]  # 누구나 view 조회 가능
    serializer_class = articleSerializer
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    permission_classes = [MyAwesomePermission]  # 로그인 된 사용자만 view 조회 가능
    # permission_classes = [RegistedMoreThanAWeekUser]
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

    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         return [RegistedMoreThanAWeekUser() for RegistedMoreThanAWeekUser in self.permission_classes]
    #     return [permissions.AllowAny()]

    def post(self, request):

        article = Article(
            writer = self.request.user,
            category = request.data.get('category', ''),
            desription = request.data.get('desription', '')
        )
        article.save()
        return article


    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})
