from rest_framework import serializers
from .models import Curse, Location, Trainer, Timetable


class CurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curse
        fields = ['title', 'description', 'photo']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'address']


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['name', 'surname', 'description']


class TimetableSerializer(serializers.ModelSerializer):
    curse = CurseSerializer()
    location = LocationSerializer()
    trainer = TrainerSerializer()

    class Meta:
        model = Timetable
        fields = ['curse', 'location', 'trainer',
                  'introductory_lecture', 'first_lesson', 'pub_date']
