from rest_framework.serializers import ModelSerializer

from .models import Sight


class SightSerializer(ModelSerializer):
    class Meta:
        model = Sight
        fields = ['title', 'category', 'views', 'full_text', 'adress', 'image_preview']
