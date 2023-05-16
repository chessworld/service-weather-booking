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
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
    day_time = serializers.PrimaryKeyRelatedField(queryset=DayTime.objects.all())
    booking_option = BookingOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'location', 'day_time', 'status', 'result', 'booking_option']


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