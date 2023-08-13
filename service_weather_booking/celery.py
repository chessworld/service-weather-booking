import os
from kombu import Exchange, Queue
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service_weather_booking.settings')

app = Celery('service_weather_booking')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(['weather_api'])

app.conf.task_queues = (
    Queue('default', Exchange('default'), routing_key='default'),
)

app.conf.beat_schedule = {
    'booking-results-scheduler': {
        'task': 'weather_api.tasks.update_bookings.update_bookings',
        # 'schedule': crontab(hour='12,16,20', minute='0'),
        'schedule': 30.0,
    },
}
