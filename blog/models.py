from django.db import models
from user.models import User


class Article(models.Model):
    writer = models.CharField("글작성자", max_length=20)
    title = models.CharField("글 제목", max_length=20, unique=True)

    category = models.ForeignKey(to="Category", verbose_name="카테고리",on_delete=models.SET_NULL,null=True, default= "카테고리 없음")
    description = models.CharField("글 설명", max_length=255)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField("카테고리 이름", max_length=20, unique=True)
    description = models.CharField("카테고리설명", max_length=255)

    def __str__(self):
        return self.name
