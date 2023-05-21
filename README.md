# Weather Booking App Service

## How to Run Development

* Activate Virtual Environment
```sh
. .venv/bin/activate 
```

* pip install
```sh
. pip install Django psycopg2 drf-yasg django-cors-headers
```

* Run Python Server
```sh
python manage.py runserver
```

* Make db migratitions
```sh
python manage.py makemigrations
python manage.py migrate
```

## Troubleshooting

### Migrations not applying
0. Connect to postgres
```
psql service_weather_booking
\c postgres
```

1. Drop the database

```sql
DROP DATABASE service_weather_booking\g
```

2. Create the database

```sql
CREATE DATABASE service_weather_booking\g
```

3. Rerun migrations
