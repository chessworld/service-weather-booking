from celery import shared_task
from django.db import transaction
from datetime import datetime

from ..models import Booking, Location, WeatherOption
from ..weather_providers import bom

import logging
logger = logging.getLogger(__name__)

@shared_task
def update_bookings():

    logger.info('Update bookings task started.')
    
    current_date = datetime.today().date()
    logger.info(f'Current date: {current_date}')
    
    bookings = Booking.objects.filter(date=current_date, status='Upcoming')
    logger.info(f'Found {bookings.count()} bookings to update.')

    with transaction.atomic():
        for booking in bookings:
            
            logger.info(f'Updating booking {booking.id} with result {booking.result} and status Completed.')
            
            result = 'Successful' if check_booking(booking) else 'Failed'
            booking.result = result
            booking.status = 'Completed'
            
            booking.save()
            logger.info(f'Booking {booking.id} result: {booking.result}')
            
    logger.info('Update bookings task finished.')


def check_booking(booking: Booking):
    booking_option = booking.weather_option
    postcode = booking.location.postcode
    
    start_hour = 8 if booking.time_period == 'Morning' else 12 if booking.time_period == 'Afternoon' else 16
    end_hour = start_hour + 4
    now = datetime.now()
    start_time = datetime(now.year, now.month, now.day, start_hour)
    end_time = datetime(now.year, now.month, now.day, end_hour)

    weather_options = bom.get_weather(start_time=start_time, end_time=end_time, postcode=postcode)
    
    portion = lambda key, val, items: len([item for item in items if item[key] == val])/len(items)
    
    if portion('weather_type', booking_option.weather, weather_options) < 0.5:
        return False
    if portion('temperature', booking_option.temperature, weather_options) < 0.5:
        return False
    if portion('wind', booking_option.wind, weather_options) < 0.5:
        return False
    
    return True