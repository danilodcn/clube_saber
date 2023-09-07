# python manage.py migrate

poetry run gunicorn explorer2go.wsgi --bind 0.0.0.0:8000
