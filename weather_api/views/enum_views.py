from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi

from ..models import WeatherOption

class Enum_Views(APIView):
    def get(self, request, *args, **kwargs):
        response = {
            'weather_option_types': {},
            'weather_option_choices': {},
            'weather_value_types': {},
        }

        for item in WeatherOption.WEATHER_OPTION_TYPES:
            response['weather_option_types'][item[0]] = item[1]

        for item in WeatherOption.WEATHER_OPTION_TYPES:
            response['weather_option_choices'][item[0]] = item[1]

        for item in WeatherOption.WEATHER_OPTION_TYPES:
            response['weather_value_types'][item[0]] = item[1]

        return Response(response)
