from rest_framework import serializers

from .models import Booking, Location, WeatherOption, User, Weather, Temperature, Wind, Feedback

# Define serializers
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'suburb', 'state', 'postcode', 'country']


class WeatherOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherOption
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    location_name = serializers.StringRelatedField(source='location.name')
    weather_option = serializers.StringRelatedField(source='weather_option.option')
    class Meta:
        model = Booking
        fields = ['id', 'guest_id', 'location', 'location_name', 'booking_date', 'weather_option', 'temperature', 'wind', 'booking_status', 'result_weather_id'] 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'completed_tutorial']


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['id', 'temperature']


class WindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wind
        fields = ['id', 'wind']


class WeatherSerializer(serializers.ModelSerializer):
    wind = WindSerializer()
    temperature = TemperatureSerializer()
    weather_option = WeatherOptionSerializer()

    class Meta:
        model = Weather
        fields = ['id', 'wind', 'temperature', 'weather_option']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'user', 'rating', 'comments']