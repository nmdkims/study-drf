from django.db import models

# Create your models here.
class homework_message(models.Model):
    message = models.CharField(max_length=200)

