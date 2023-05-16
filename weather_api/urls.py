from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views



# urlpatterns = [
#     path('bookings/', views.BookingList.as_view(), name='booking-list'),
#     path('bookings/<str:pk>/', views.BookingDetail.as_view(), name='booking-detail'),
#     path('locations/', views.LocationList.as_view(), name='location-list'),
#     path('weather_options/', views.WeatherOptionList.as_view()),
# ]

schema_view = get_schema_view(
    openapi.Info(
        title="Weather Booking Service API",
        default_version="v1",
        description="API Endpoints Weather Booking Service",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Define URL routes
urlpatterns = [
    path('users/', views.UserView.as_view(), name='users'),
    path('users/<str:user_id>/', views.UserView.as_view(), name='user_detail'),
    path('bookings/options', views.BookingOptionsView.as_view(), name='booking_options'),
    path('bookings/', views.BookingView.as_view(), name='bookings'),
    path('bookings/<str:booking_id>/', views.BookingDetailView.as_view(), name='booking_detail'),
    # path('users/<str:user_id>/bookings/', views.UserBookingsView.as_view(), name='user_bookings'),
    path('locations/', views.LocationSearchView.as_view(), name='location_search'),
    # path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]