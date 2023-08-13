from celery import shared_task
from django.db import transaction
from datetime import datetime

from ..models import Booking, Location, WeatherOption

import logging
logger = logging.getLogger(__name__)

@shared_task()
def update_bookings():

    logger.info('Update bookings task started.')
    
    current_date = datetime.today().date()
    logger.info(f'Current date: {current_date}')
    
    bookings = Booking.objects.filter(date=current_date, status='Upcoming')
    logger.info(f'Found {bookings.count()} bookings to update.')

    with transaction.atomic():
        for booking in bookings:
            
            logger.info(f'Updating booking {booking.id} with result {booking.result} and status Completed.')
            
            result = 'Successful'
            booking.result = result
            booking.status = 'Completed'
            
            booking.save()
            logger.info(f'Booking {booking.id} result: {booking.result}')
            
    logger.info('Update bookings task finished.')