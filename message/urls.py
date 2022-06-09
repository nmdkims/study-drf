from django.urls import path, include
from .views import messageAPI

urlpatterns = [
    path("basic/", messageAPI)
]