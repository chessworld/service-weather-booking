# Weather Booking App Service

## Requirements

- Python (tested with 3.10)
- [Postgres](https://www.postgresql.org/download/)
- [Redis](https://redis.io/docs/getting-started/installation/)

## How to Run Development

#### 1. Activate virtual environment

```sh
.venv/bin/activate 
```

#### 2. Install requirements

```sh
pip install -r requirements.txt
```

#### 3. Make db migratitions

```sh
python manage.py makemigrations
python manage.py migrate
```

#### 4. Run Pytest

```sh
pytest --ds=service_weather_booking.settings --disable-warnings
```

#### 5. Run Python server

```sh
python manage.py runserver
```

#### 6. Run Celery

###### 6.1 Start Redis

Install Redis (for WSL)

```sh
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
```

Start the Redis server

```sh
sudo service redis-server start
```

###### 6.2 Start Celery

Open two new terminal instances and run:

```sh
python -m celery -A service_weather_booking worker -l info --pool=solo
```

```sh
python -m celery -A service_weather_booking beat -l info
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
