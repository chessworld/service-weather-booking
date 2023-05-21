from rest_framework import status, views
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..models import User, Booking, BookingOption
from ..serializers import UserSerializer, BookingSerializer, BookingOptionSerializer


class BookingOptionList(views.APIView):
    @swagger_auto_schema(responses={200: BookingOptionSerializer(many=True)})
    def get(self, request, format=None):
        booking_options = BookingOption.objects.all()
        serializer = BookingOptionSerializer(booking_options, many=True)
        return Response(serializer.data)


class BookingRetrieve(views.APIView):
    @swagger_auto_schema(responses={200: BookingSerializer})
    def get(self, request, booking_id, format=None):
        booking = Booking.objects.prefetch_related('bookingoption_set').get(id=booking_id)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

class BookingList(views.APIView):
    @swagger_auto_schema(responses={200: BookingOptionSerializer})
    def get(self, request, format=None):
        bookingoptions = BookingOption.objects.all()
        serializer = BookingOptionSerializer(bookingoptions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookingCreate(views.APIView):
    @swagger_auto_schema(request_body=BookingOptionSerializer)
    def post(self, request, format=None):
        serializer = BookingOptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


class BookingUpdate(views.APIView):
    @swagger_auto_schema(request_body=BookingSerializer)
    def patch(self, request, booking_id, format=None):
        pass
        # booking = Booking.objects.get(id=booking_id)
        # serializer = BookingSerializer(booking, data=request.data, partial=True)  # set partial=True to update a data partially
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
