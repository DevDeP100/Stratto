release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn core.wsgi --bind 0.0.0.0:$PORT 