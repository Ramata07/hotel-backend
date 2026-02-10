import logging
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Hotel
from .serializers import HotelSerializer

logger = logging.getLogger(__name__)

class HotelViewSet(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    
    # ⚠️ CRITIQUE : Ajouter les parsers pour accepter les fichiers
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    def get_serializer_context(self):
        # Important pour que image_url fonctionne
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        logger.info("Response data (list): %s", response.data)
        return response
    
    def create(self, request, *args, **kwargs):
        print("=" * 50)
        print("📥 Request.data:", dict(request.data))
        print("📎 Request.FILES:", dict(request.FILES))
        print("=" * 50)
        
        response = super().create(request, *args, **kwargs)
        
        print("✅ Hôtel créé:", response.data)
        print("=" * 50)
        return response
