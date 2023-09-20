from rest_framework import status, views
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from ..models import User
from ..serializers import UserSerializer


class UserCreate(views.APIView):
    @swagger_auto_schema(
        security=[{'IsAdminUser':[]}],
        request_body=UserSerializer
        )
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(responses={200: UserSerializer})
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetail(views.APIView):
    @swagger_auto_schema(responses={200: UserSerializer})
    def get(self, request, user_id, format=None):
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    
    @swagger_auto_schema(request_body=UserSerializer)
    def patch(self, request, user_id, format=None):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)