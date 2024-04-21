from rest_framework import serializers
from .models import Super_memory


class Super_memorySerializer(serializers.ModelSerializer):
    location_name = serializers.SerializerMethodField()
    location_address = serializers.SerializerMethodField()
    link_name = serializers.SerializerMethodField()

    class Meta:
        model = Super_memory
        fields = ['location_name', 'location_address', 'date', 'link_name']

    def get_location_name(self, obj):
        return obj.location.name

    def get_location_address(self, obj):
        return obj.location.address

    def get_link_name(self, obj):
        return [link.url for link in obj.link.all()]
