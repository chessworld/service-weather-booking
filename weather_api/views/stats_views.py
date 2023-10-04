from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import views
from rest_framework.response import Response
from datetime import datetime, timedelta

from ..models import Booking
from ..serializers import BookingSerizalizerStats


DAYS_SINCE_BOOKING = 30


class StatsGetResource(views.APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('start_date', in_=openapi.IN_QUERY, type='string', description='Start date for filtering bookings', format='date'),
            openapi.Parameter('end_date', in_=openapi.IN_QUERY, type='string', description='End date for filtering bookings', format='date'),
            openapi.Parameter('country', in_=openapi.IN_QUERY, type='string', description='Country for filtering bookings'),
            openapi.Parameter('state', in_=openapi.IN_QUERY, type='string', description='State for filtering bookings'),
        ],
        responses={200: BookingSerizalizerStats(many=True)}
    )
    def get(self, request, format=None):
        start_date = request.query_params.get('start_date', datetime.now() - timedelta(days=DAYS_SINCE_BOOKING))
        end_date = request.query_params.get('end_date', datetime.now())

        country = request.query_params.get('country', None)
        state = request.query_params.get('state', None)

        if country and state:
            bookings = Booking.objects.filter(date__gte=start_date, date__lte=end_date, country=country, state=state)
        elif country:
            bookings = Booking.objects.filter(date__gte=start_date, date__lte=end_date, country=country)
        else:
            bookings = Booking.objects.filter(date__gte=start_date, date__lte=end_date)

        serializer = BookingSerizalizerStats(bookings, many=True)
        return Response(serializer.data)
