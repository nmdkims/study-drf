from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import ActorView

urlpatterns = [
    path('actor/', ActorView.as_view())
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
