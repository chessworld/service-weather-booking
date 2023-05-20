from rest_framework import serializers
from .models import User, Booking, Location, DayTime, WeatherOption, BookingOption, ActualWeather, Feedback# Define the serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'completed_tutorial']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['suburb', 'state', 'postcode', 'country']


class DayTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayTime
        fields = ['date', 'time_period', 'start_time', 'end_time']

class WeatherOptionSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    day_time = DayTimeSerializer()

    class Meta:
        model = WeatherOption
        fields = ['option_type', 'option_name', 'value_type', 'min_value', 'max_value', 'location', 'day_time']


class BookingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingOption
        fields = ['booking', 'weather_option']


class BookingSerializer(serializers.ModelSerializer):
    day_time = DayTimeSerializer()

    class Meta:
        model = Booking
        fields = ['id', 'user', 'location', 'day_time', 'status', 'result']

    def create(self, validated_data):
        day_time_data = validated_data.pop('day_time')
        day_time = DayTime.objects.create(**day_time_data)
        booking = Booking.objects.create(day_time=day_time, **validated_data)
        return booking


class ActualWeatherSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    datetime = DayTimeSerializer()

    class Meta:
        model = ActualWeather
        fields = ['location', 'datetime']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'rating', 'comment']
