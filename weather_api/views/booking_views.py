from rest_framework import status, views
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from ..serializers import BookingSerializer
from ..models import Booking


class BookingGetPatchResource(views.APIView):
    @swagger_auto_schema(responses={200: BookingSerializer})
    def get(self, request, booking_id, format=None):
        booking = Booking.objects.prefetch_related('bookingoption_set').get(id=booking_id)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=BookingSerializer)
    def patch(self, request, booking_id, format=None):
        booking = Booking.objects.get(id=booking_id)
        serializer = BookingSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingList(views.APIView):
    @swagger_auto_schema(responses={200: BookingSerializer(many=True)})
    def get(self, request, user_id, format=None):
        bookings = Booking.objects.filter(user__id=user_id)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)


class BookingCreate(views.APIView):
    @swagger_auto_schema(request_body=BookingSerializer)
    def post(self, request, format=None):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
