from django.conf import settings
from django.urls import path
from .views import HotelViewSet
from django.conf.urls.static import static
from .views import chat_gemini

urlpatterns = [
    path('hotels/', HotelViewSet.as_view(), name='hotel-list-create'),
    path('chat/', chat_gemini, name='chat_gemini'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)