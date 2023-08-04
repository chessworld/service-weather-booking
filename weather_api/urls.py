from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import BookingCreate, UserCreate, UserDetail, LocationSearch, FeedbackCreate, Enum_Views, BookingGetPatchResource, BookingList


schema_view = get_schema_view(
    openapi.Info(
        title="Weather App API",
        default_version='v1',
        description="API endpoints for the Weather App",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('users/', UserCreate.as_view(), name='user_create'),
    path('users/<uuid:user_id>/', UserDetail.as_view(), name='user_detail'),
    
    path('bookings/', BookingCreate.as_view(), name='booking_create'),
    path('bookings/<uuid:booking_id>/', BookingGetPatchResource.as_view(), name='booking_get_patch_resouce'),
    path('bookings/<uuid:user_id>/', BookingList.as_view(), name='user_booking_list'),
    # path('bookings/options', BookingOptionList.as_view(), name='booking_option_list'),
    
    path('locations/', LocationSearch.as_view(), name='location_search'),
    
    path('feedback/', FeedbackCreate.as_view(), name='feedback_create'),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('enums/', Enum_Views.as_view(), name='weather-options')
]
