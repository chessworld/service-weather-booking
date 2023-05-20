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
    class Meta:
        model = WeatherOption
        fields = ['option_type', 'option_name', 'value_type', 'min_value', 'max_value']


class BookingSerializer(serializers.ModelSerializer):
    day_time = DayTimeSerializer()

    class Meta:
        model = Booking
        fields = ['id', 'user', 'location', 'day_time', 'status', 'result']


class BookingOptionSerializer(serializers.ModelSerializer):
    booking = BookingSerializer(many=True)

    weather_option = WeatherOptionSerializer(many=True)

    class Meta:
        model = BookingOption
        fields = ['booking', 'weather_option']

    def create(self, validated_data):
        booking_data = validated_data.pop('booking')
        weather_option_data = validated_data.pop('weather_option')

        booking_option = BookingOption.objects.create()

        for booking in booking_data:
            day_time_data = booking.pop('day_time')
            day_time_obj = DayTime.objects.create(**day_time_data)
            booking_obj = Booking.objects.create(day_time=day_time_obj, **booking)
            booking_option.booking.add(booking_obj)

        for weather_option in weather_option_data:
            weather_option_obj = WeatherOption.objects.create(**weather_option)
            booking_option.weather_option.add(weather_option_obj)

        return booking_option


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
