from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import BookingOptionList, BookingCreate, BookingUpdate, BookingRetrieve,  UserCreate, UserRetrieve, UserBookingList, LocationSearch, FeedbackCreate, Enum_Views


schema_view = get_schema_view(
    openapi.Info(
        title="Weather App API",
        default_version='v1',
        description="API endpoints for the Weather App",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# Define URL routes
urlpatterns = [
    path('users/', UserCreate.as_view(), name='user_create'),
    path('users/<uuid:user_id>/', UserRetrieve.as_view(), name='user_detail'),
    path('users/<uuid:user_id>/bookings/', UserBookingList.as_view(), name='user_booking_list'),
    path('bookings/', BookingCreate.as_view(), name='booking_create'),
    path('bookings/options', BookingOptionList.as_view(), name='booking_option_list'),
    path('bookings/<uuid:booking_id>/', BookingRetrieve.as_view(), name='booking_detail'),
    path('bookings/<uuid:booking_id>/', BookingUpdate.as_view(), name='booking_update'),
    path('locations/', LocationSearch.as_view(), name='location_search'),
    path('feedback/', FeedbackCreate.as_view(), name='feedback_create'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('enums/', Enum_Views.as_view(), name='weather-options')
]
