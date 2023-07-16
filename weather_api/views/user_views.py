from rest_framework import status, views
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..models import User, Booking
from ..serializers import UserSerializer, BookingSerializer


class UserCreate(views.APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdate(views.APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request, user_id, format=None):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieve(views.APIView):
    @swagger_auto_schema(responses={200: UserSerializer})
    def get(self, request, user_id, format=None):
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserBookingList(views.APIView):
    @swagger_auto_schema(responses={200: BookingSerializer(many=True)})
    def get(self, request, user_id, format=None):
        bookings = Booking.objects.filter(user__id=user_id)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
