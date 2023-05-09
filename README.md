# Weather Booking App Service

## How to Run Development

* Activate Virtual Environment
```sh
. .venv/bin/activate 
```

* pip install
```sh
. pip install Django psycopg2 django-rest-swagger drf-yasg
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