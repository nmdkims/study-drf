from django.db import models
from user.models import User


class Actor(models.Model):
    actorname = models.CharField("성우이름", max_length=20, unique=True)
    writer = models.CharField("제작자", max_length=20)
    category = models.ManyToManyField(to="Category", verbose_name="카테고리", default= "카테고리 없음")
    voice = models.ImageField(upload_to="%Y/%m/%d")

    def __str__(self):
        return self.actorname

class Category(models.Model):
    categoryname = models.CharField("카테고리 이름", max_length=20, unique=True)

    def __str__(self):
        return self.categoryname
