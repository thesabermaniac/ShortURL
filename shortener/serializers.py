from .models import ShortURL
from rest_framework import serializers


class ShortURLSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializes the ShortURL fields for API calls
    """
    class Meta:
        model = ShortURL
        fields = ['id', 'url', 'hit_count']
