from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.CharField(verbose_name="제목", max_length=20)
    thumbnail = models.ImageField(upload_to="%Y/%m/%d")
    description = models.CharField("설명", max_length=255)
    created = models.DateTimeField(auto_now_add=True, verbose_name="등록일자")
    expose_startdate = models.DateTimeField(verbose_name="노출 시작 일")
    expose_enddate = models.DateTimeField(verbose_name="노출 종료 일")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
