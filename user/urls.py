from django.urls import path, include
from .views import UserApiView

urlpatterns = [
    path("user/", UserApiView.as_view())
]