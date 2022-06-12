from django.urls import path
from .views import ArticleView

urlpatterns = [
    path("blog/", ArticleView.as_view())
]