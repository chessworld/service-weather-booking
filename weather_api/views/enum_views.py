from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import WeatherOption

class Enum_Views(APIView):
    def get(self, request, *args, **kwargs):
        response = {
            'weather_option_types': {},
            'weather_option_choices': {},
            'weather_value_type': {},
        }

        for item in WeatherOption.WEATHER_OPTION_TYPES:
            response['weather_option_types'][item[0]] = item[1]

        for item in WeatherOption.WEATHER_OPTION_CHOICES:
            response['weather_option_choices'][item[0]] = item[1]

        for item in WeatherOption.WEATHER_VALUE_TYPE:
            response['weather_value_type'][item[0]] = item[1]

        return Response(response)
