from rest_framework import serializers
from .models import Super_memory


class Super_memorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Super_memory
        fields = ['location', 'date']
