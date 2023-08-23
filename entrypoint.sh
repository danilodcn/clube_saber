python manage.py migrate

poetry run gunicorn clube_saber.wsgi --bind 0.0.0.0:8000
