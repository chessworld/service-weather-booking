from rest_framework import serializers

from .models import User, Booking, Location, WeatherOption, ActualWeather, Feedback


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
    weather_option = WeatherOptionSerializer()

    class Meta:
        model  = Booking
        fields = ['id', 'user', 'location', 'date', 'time_period', 'weather_option', 'status', 'result']

    def create(self, validated_data):
        weather_option_data = validated_data.pop('weather_option')
        weather_option      = WeatherOption.objects.create(**weather_option_data)

        return Booking.objects.create(weather_option=weather_option, **validated_data)

    def update(self, instance, validated_data):
        weather_option_data = validated_data.pop('weather_option', None)
        instance = super().update(instance, validated_data)

        if weather_option_data:
            weather_option = instance.weather_option
            for key, value in weather_option_data.items():
                setattr(weather_option, key, value)
            weather_option.save()

        return instance


class ActualWeatherSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model  = ActualWeather
        fields = ['location', 'datetime']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Feedback
        fields = ['id', 'rating', 'comment']
