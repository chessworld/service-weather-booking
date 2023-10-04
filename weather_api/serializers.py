from rest_framework import serializers

from .models import User, Booking, Location, WeatherOption, ActualWeather, Feedback
from .services.bom import Bom


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'name', 'completed_tutorial']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Location
        fields = ['suburb', 'state', 'postcode', 'country']


class WeatherOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = WeatherOption
        fields = ['weather', 'wind', 'temperature']


class BookingSerializer(serializers.ModelSerializer):
    weather_option      = WeatherOptionSerializer()
    location            = LocationSerializer()
    location_provider   = Bom()

    class Meta:
        model  = Booking
        fields = ['id', 'user', 'booking_name', 'location', 'date', 'time_period', 'weather_option', 'status', 'result']

    def create(self, validated_data):
        weather_option_data = validated_data.pop('weather_option')
        weather_option      = WeatherOption.objects.get_or_create(**weather_option_data)

        location_data       = validated_data.pop('location')
        location            = self.location_provider.get_location(**location_data)

        return Booking.objects.create(location=location[0], weather_option=weather_option[0], **validated_data)

    def update(self, instance, validated_data):
        weather_option_data = validated_data.pop('weather_option', None)
        instance = super().update(instance, validated_data)

        if weather_option_data:
            weather_option = instance.weather_option
            for key, value in weather_option_data.items():
                setattr(weather_option, key, value)
            weather_option.save()

        return instance


class BookingSerizalizerStats(BookingSerializer):

    class Meta:
        model = Booking
        fields = ['location', 'date', 'time_period', 'weather_option', 'status', 'result']


class ActualWeatherSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model  = ActualWeather
        fields = ['location', 'datetime']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Feedback
        fields = ['id', 'rating', 'comment']
