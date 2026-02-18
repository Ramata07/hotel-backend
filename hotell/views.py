import logging
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Hotel
from .serializers import HotelSerializer
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings


logger = logging.getLogger(__name__)

class HotelViewSet(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    
    
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

@api_view(['POST'])
def chat_gemini(request):
    """
    Vue Django pour interagir avec le chatbot Gemini.
    Attend un JSON avec { "content": "message utilisateur" }
    Renvoie { "reply": "réponse du bot" }
    """
    user_message = request.data.get("content", "").strip()
    if not user_message:
        return Response({"reply": "Veuillez entrer un message."})

    # Endpoint officiel Gemini (Google)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={settings.API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [{"text": user_message}]
            }
        ]
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()

        # Extraire le texte renvoyé par Gemini
        reply = data["candidates"][0]["content"]["parts"][0]["text"]

        return Response({"reply": reply})

    except Exception as e:
        return Response({"reply": f"Erreur du serveur: {str(e)}"})