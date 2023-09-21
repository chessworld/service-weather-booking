from rest_framework import status, views
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..models.location import Location
from ..serializers import LocationSerializer
from ..services import LocationProvider, Bom

NUM_LOCATION_SUGGESTIONS = 5

class LocationSearch(views.APIView):
    
    def __init__(self):
        self.location_provider = Bom()


    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('query', openapi.IN_QUERY,
                              type='string',
                              description='Search query. Can be suburb name or postcode. Must be at least 4 characters'),
        ],
        responses={200: LocationSerializer(many=True)}
    )
    def get(self, request, format=None):
        response_data = []

        query = request.query_params.get('query', None)
        if query and len(query) > 3:
            existing_locations = Location.objects.filter(suburb__icontains=query)
            if existing_locations.exists():
                for location in existing_locations[:min(len(existing_locations), 4)]:
                    response_data.append({
                        'suburb': location.suburb,
                        'postcode': location.postcode,
                        'state': location.state,
                        'country': location.country
                    })
                if len(response_data) >= NUM_LOCATION_SUGGESTIONS:
                    return Response(response_data, status=status.HTTP_200_OK)

            location_results = self.location_provider.search_location(search=query)
            for location in location_results:
                location = {
                        'suburb': location['name'],
                        'postcode': location['postcode'],
                        'state': location['state'],
                        'country': location['country']
                    }
                if location not in response_data:
                    response_data.append(location)
                if len(response_data) >= NUM_LOCATION_SUGGESTIONS:
                    break
            return Response(response_data, status=status.HTTP_200_OK)
        return Response('Query should be at least 4 characters',status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=LocationSerializer)
    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)