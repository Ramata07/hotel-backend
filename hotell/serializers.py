from rest_framework import serializers
from .models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = '__all__'

    def get_image(self, obj):
        if not obj.image:
            return None
        try:
            url = obj.image.url
            # Si l'URL est relative, la rendre absolue
            if url and url.startswith('/'):
                request = self.context.get('request')
                if request:
                    return request.build_absolute_uri(url)
            return url  # Déjà une URL complète (ex: Cloudinary)
        except (ValueError, AttributeError):
            return None