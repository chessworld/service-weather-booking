from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, views
from rest_framework.response import Response

from ..serializers import BookingSerializer
from ..models import Booking, User


class BookingGetPatchResource(views.APIView):
    @swagger_auto_schema(responses={200: BookingSerializer})
    def get(self, request, booking_id, format=None):
        booking = Booking.objects.get(id=booking_id)
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


class BookingGetPostResource(views.APIView):
    @swagger_auto_schema(responses={200: BookingSerializer(many=True)})
    def get(self, request, user_id, format=None):
        bookings = Booking.objects.filter(user__id=user_id)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=BookingSerializer)
    def post(self, request, user_id, format=None):
        user = get_object_or_404(User, id=user_id)
        data = request.data.copy()
        data['user'] = user.id

        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)