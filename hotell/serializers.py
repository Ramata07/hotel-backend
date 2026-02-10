from rest_framework import serializers
from .models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Hotel
        fields = '__all__'
    
    def get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            
            if url.startswith('http://'):
                url = url.replace('http://', 'https://', 1)
            return url
        return None