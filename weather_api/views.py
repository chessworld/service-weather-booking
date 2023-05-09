from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import LocationSerializer, WeatherOptionSerializer, BookingSerializer, UserSerializer, TemperatureSerializer, WindSerializer, WeatherSerializer, FeedbackSerializer
from .models import Booking, Location, WeatherOption, User, Weather, Temperature, Wind, Feedback



# class BookingList(generics.ListCreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer

#     def get_queryset(self):
#         guest_id = self.request.query_params.get('guest_id', None)
#         if guest_id:
#             return Booking.objects.filter(guest_id=guest_id)
#         return Booking.objects.all()

#     def post(self, request, *args, **kwargs):
#         # Create a new booking with the provided data
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer

#     def get(self, request, *args, **kwargs):
#         # Retrieve a specific booking
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

#     def patch(self, request, *args, **kwargs):
#         # Update a specific booking with the provided data
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, *args, **kwargs):
#         # Delete a specific booking
#         instance = self.get_object()
#         instance.delete()
#         return Response({"message": "Booking deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


# class LocationList(generics.ListAPIView):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer


# class WeatherOptionList(generics.ListAPIView):
#     queryset = WeatherOption.objects.all()
#     serializer_class = WeatherOptionSerializer


# Define views
class UserView(views.APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Generate a unique guest ID for a new user and store it in the database.",
        responses={200: openapi.Response('Response', UserSerializer)}
    )
    def post(self, request):
        # Generate a unique guest ID
        # This is a placeholder implementation and should be replaced with actual logic
        guest_id = 'unique-guest-id'

        # Create a new user
        user = User.objects.create(name=guest_id)

        # Serialize the user
        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_description="Retrieve the details of a user.",
        responses={200: openapi.Response('Response', UserSerializer)}
    )
    def get(self, request, guest_id):
        # Get the user
        user = User.objects.get(name=guest_id)

        # Serialize the user
        serializer = UserSerializer(user)

        return Response(serializer.data)


class BookingOptionsView(views.APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve available weather options for a specific location, date, and period of day.",
        manual_parameters=[
            openapi.Parameter('location', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('date', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('period', openapi.IN_QUERY, type=openapi.TYPE_STRING)
        ],
        responses={200: openapi.Response('Response', BookingSerializer)}
    )
    def get(self, request):
        # Get the query parameters
        location = request.query_params.get('location')
        date = request.query_params.get('date')
        period = request.query_params.get('period')

        # Get the available weather options
        # This is a placeholder implementation and should be replaced with actual logic
        weather_options = WeatherOption.objects.all()
        temperature_options = Temperature.objects.all()
        wind_options = Wind.objects.all()

        # Serialize the options
        weather_serializer = WeatherOptionSerializer(weather_options, many=True)
        temperature_serializer = TemperatureSerializer(temperature_options, many=True)
        wind_serializer = WindSerializer(wind_options, many=True)

        return Response({
            'weather_options': weather_serializer.data,
            'temperature_options': temperature_serializer.data,
            'wind_options': wind_serializer.data
        })


class BookingView(views.APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Create a new weather booking with the provided weather, temperature, wind, location, and date/time.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'guest_id': openapi.Schema(type=openapi.TYPE_STRING, description='Guest ID'),
                'weather': openapi.Schema(type=openapi.TYPE_STRING, description='Weather option'),
                'temperature': openapi.Schema(type=openapi.TYPE_STRING, description='Temperature option'),
                'wind': openapi.Schema(type=openapi.TYPE_STRING, description='Wind option'),
                'location': openapi.Schema(type=openapi.TYPE_STRING, description='Location suburb'),
                'date': openapi.Schema(type=openapi.TYPE_STRING, description='Booking date'),
                'period': openapi.Schema(type=openapi.TYPE_STRING, description='Time period'),
                'event_name': openapi.Schema(type=openapi.TYPE_STRING, description='Event name')
            }
        ),
        responses={201: openapi.Response('Response', BookingSerializer)}
    )
    def post(self, request):
        # Get the request data
        data = request.data

        # Get the user
        user = User.objects.get(name=data['guest_id'])

        # Get the weather
        weather_option = WeatherOption.objects.get(weather_option=data['weather'])
        temperature = Temperature.objects.get(temperature=data['temperature'])
        wind = Wind.objects.get(wind=data['wind'])
        weather = Weather.objects.create(wind=wind, temperature=temperature, weather_option=weather_option)

        # Get the location
        location = Location.objects.get(suburb=data['location'])

        # Create the booking
        booking = Booking.objects.create(user=user, weather=weather, location=location, date=data['date'], status='Upcoming')

        # Serialize the booking
        serializer = BookingSerializer(booking)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookingDetailView(views.APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Retrieve the details of a booking.",
        responses={200: openapi.Response('Response', BookingSerializer)}
    )
    def get(self, request, booking_id):
        # Get the booking
        booking = Booking.objects.get(id=booking_id)

        # Serialize the booking
        serializer = BookingSerializer(booking)

        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Update booking details, such as result status (success/failure).",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'status': openapi.Schema(type=openapi.TYPE_STRING, description='New booking status'),
                'result': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='New booking result')
            }
        ),
        responses={200: openapi.Response('Response', BookingSerializer)}
    )
    def put(self, request, booking_id):
        # Get the request data
        data = request.data

        # Get the booking
        booking = Booking.objects.get(id=booking_id)

        # Update the booking
        booking.status = data.get('status', booking.status)
        booking.result = data.get('result', booking.result)
        booking.save()

        # Serialize the booking
        serializer = BookingSerializer(booking)

        return Response(serializer.data)


class LocationSearchView(views.APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="Search for locations by text input, returning a list of matching suburbs.",
        manual_parameters=[
            openapi.Parameter('query', openapi.IN_QUERY, type=openapi.TYPE_STRING)
        ],
        responses={200: 'location list'}
    )
    def get(self, request):
        # Get the query parameter
        query = request.query_params.get('query')

        # Search for locations
        # This is a placeholder implementation and should be replaced with actual logic
        locations = Location.objects.filter(suburb__icontains=query)

        # Serialize the locations
        serializer = LocationSerializer(locations, many=True)

        return Response({'locations': [location['suburb'] for location in serializer.data]})


# class FeedbackView(views.APIView):
#     permission_classes = [AllowAny]

#     @swagger_auto_schema(
#         operation_description="Submit user feedback and 'buy me a coffee' responses.",
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             properties={
#                 'guest_id': openapi.Schema(type=openapi.TYPE_STRING, description='Guest ID'),
#                 'feedback': openapi.Schema(type=openapi.TYPE_STRING, description='User feedback'),
#                 'coffee_response': openapi.Schema(type=openapi.TYPE_STRING, description='User coffee response')
#             }
#         ),
#         responses={201: openapi.Response('Response', FeedbackSerializer)}
#     )
#     def post(self, request):
#         # Get the request data
#         data = request.data

#         # Get the user
#         user = User.objects.get(name=data['guest_id'])

#         # Create the feedback
#         feedback = Feedback.objects.create(user=user, rating=data['feedback'], comments=data['coffee_response'])

#         # Serialize the feedback
#         serializer = FeedbackSerializer(feedback)

#         return Response(serializer.data, status=status.HTTP_201_CREATED)