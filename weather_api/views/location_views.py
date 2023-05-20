from rest_framework import status, views
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..models.location import Location
from ..serializers import LocationSerializer


class LocationSearch(views.APIView):
    @swagger_auto_schema(responses={200: LocationSerializer(many=True)})
    def get(self, request, format=None):
        state = request.query_params.get('state', None)
        if (state != None):
            locations = Location.objects.filter(suburb__icontains=state)
        else:
            locations = Location.objects
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
