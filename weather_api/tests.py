from django.test import TestCase, Client
from django.urls import reverse
from .serializers import LocationSerializer, WeatherOptionSerializer, BookingSerializer, UserSerializer, TemperatureSerializer, WindSerializer, WeatherSerializer
from .models import Booking, Location, WeatherOption, User, Weather, Temperature, Wind



class UserTestCase(TestCase):
    def setUp(self):
        # Set up the test case by creating a client object and a user object
        self.client = Client()  # Instantiate a client object for making HTTP requests
        self.user1 = User.objects.create(name='User One')  # Create a user object with the name 'User One'

    def test_get_user(self):
        # Make a GET request to the 'user_detail' URL, passing the user's ID as a parameter
        response = self.client.get(reverse('user_detail', kwargs={'user_id': self.user1.id}))
        # Assert that the response status code is 200 (successful)
        self.assertEqual(response.status_code, 200)
        # Assert that the response data matches the serialized data of the user object
        self.assertEqual(response.data, UserSerializer(self.user1).data)


class WeatherOptionsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_weather_options(self):
        response = self.client.get(reverse('booking_options'))
        self.assertEqual(response.status_code, 200)
        expected_data = {
            'weather_options': ['Sunny', 'Rainy', 'Cloudy', 'Stormy'],
            'temperature_options': ['Cool', 'Mild', 'Warm', 'Hot', 'Freezing'],
            'wind_options': ['No Wind', 'Calm', 'Windy', 'Gusty']
        }
        self.assertEqual(response.data, expected_data)


class BookingTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create(name='User One')
        self.location1 = Location.objects.create(suburb='suburb1', state='ST', postcode='1234', country='Country')
        self.weather_option1 = WeatherOption.objects.create(weather_option='Sunny')
        self.temperature1 = Temperature.objects.create(temperature='Cool')
        self.wind1 = Wind.objects.create(wind='No Wind')
        self.weather1 = Weather.objects.create(wind=self.wind1, temperature=self.temperature1, weather_option=self.weather_option1)
        self.booking1 = Booking.objects.create(
            user=self.user1,
            weather=self.weather1,
            location=self.location1,
            date='2023-05-15'
        )
        print("HERE")
        print(self.booking1.id)
        print("DONE")

    def test_post_booking(self):
        data = {
            'user': self.user1.id,
            'weather': self.weather1.id,
            'location': self.location1.id,
            'date': '2023-05-15',
        }
        response = self.client.post(reverse('bookings'), data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data, BookingSerializer(self.booking1).data)

    def test_get_booking(self):
        response = self.client.get(reverse('booking_detail', kwargs={'booking_id': self.booking1.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, BookingSerializer(self.booking1).data)

    def test_get_user_bookings(self):
        response = self.client.get(reverse('user_bookings', kwargs={'user_id': self.user1.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'bookings': [BookingSerializer(self.booking1).data]})

    def test_put_booking(self):
        data = {'status': 'Completed', 'result': True}
        response = self.client.put(reverse('booking_detail', kwargs={'booking_id': self.booking1.id}), data)
        self.booking1.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, BookingSerializer(self.booking1).data)


class LocationTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_locations(self):
        response = self.client.get(reverse('location_search'), {'query': 'suburb'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'locations': [LocationSerializer(location).data for location in Location.objects.filter(suburb__icontains='suburb')]})

# class FeedbackTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user1 = User.objects.create(name='User One')
#         self.feedback1 = Feedback.objects.create(location=self.user1, rating='Good', comments='Great app')

#     def test_post_feedback(self):
#         data = {
#             'location': self.user1.id,
#             'rating': 'Good',
#             'comments': 'Great app'
#         }
#         response = self.client.post(reverse('feedback'), data)
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(response.data, FeedbackSerializer(self.feedback1).data)

