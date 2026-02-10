from django.conf import settings
from django.urls import path
from .views import HotelViewSet
from django.conf.urls.static import static

urlpatterns = [
    path('hotels/', HotelViewSet.as_view(), name='hotel-list-create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)