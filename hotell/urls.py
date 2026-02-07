from rest_framework.routers import DefaultRouter
from .views import HotelViewSet

routeur = DefaultRouter()
routeur.register(r'hotels',HotelViewSet)
urlpatterns = routeur.urls

