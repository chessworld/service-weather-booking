from rest_framework import status, views
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..models.location import Location
from ..serializers import LocationSerializer


class LocationSearch(views.APIView):
    @swagger_auto_schema(responses={200: LocationSerializer(many=True)})
    def get(self, request, format=None):
        query = request.query_params.get('query', '')
        locations = Location.objects.filter(suburb__icontains=query)
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)