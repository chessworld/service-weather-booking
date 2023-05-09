from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from . import views



# urlpatterns = [
#     path('bookings/', views.BookingList.as_view(), name='booking-list'),
#     path('bookings/<str:pk>/', views.BookingDetail.as_view(), name='booking-detail'),
#     path('locations/', views.LocationList.as_view(), name='location-list'),
#     path('weather_options/', views.WeatherOptionList.as_view()),
# ]

schema_view = get_swagger_view(title='API')

# Define URL routes
urlpatterns = [
    path('users/', views.UserView.as_view(), name='users'),
    path('users/<str:guest_id>/', views.UserView.as_view(), name='user_detail'),
    path('bookings/options', views.BookingOptionsView.as_view(), name='booking_options'),
    path('bookings/', views.BookingView.as_view(), name='bookings'),
    path('bookings/<str:booking_id>/', views.BookingDetailView.as_view(), name='booking_detail'),
    path('users/<str:guest_id>/bookings/', views.UserBookingsView.as_view(), name='user_bookings'),
    path('locations/', views.LocationSearchView.as_view(), name='location_search'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    path('', schema_view),
]