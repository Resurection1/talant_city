from rest_framework import serializers
from .models import Super_memory


class Super_memorySerializer(serializers.ModelSerializer):
    location_name = serializers.SerializerMethodField()

    class Meta:
        model = Super_memory
        fields = ['location_name', 'date']

    def get_location_name(self, obj):
        return obj.location.name
