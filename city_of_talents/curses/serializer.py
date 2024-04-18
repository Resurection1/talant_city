from rest_framework import serializers
from .models import Curse, Location, Trainer, Timetable, Sign_up_for_a_course

from django.core.validators import RegexValidator


class CurseSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField('get_photo')

    class Meta:
        model = Curse
        fields = ['title', 'description_comment', 'photo']

    def get_photo(self, curse):
        request = self.context.get('request')
        if request and curse.photo:
            return request.build_absolute_uri(curse.photo.url)
        return None


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


class Sign_up_for_a_courseSerializer(serializers.ModelSerializer):
    phone_number_validator = RegexValidator(
        regex=r"^\d+$", message="Введите только цифры без лишних символов")

    class Meta:
        model = Sign_up_for_a_course
        fields = ['name', 'phone_number', 'email', 'curse', 'customer_comment']

    def validate_phone_number(self, value):
        self.phone_number_validator(value)
        return value

    def validate(self, attrs):
        # Call the superclass validate method to perform any other validations
        return super().validate(attrs)
