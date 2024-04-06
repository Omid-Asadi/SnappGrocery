#!/bin/sh

echo "[Start script]"
python manage.py migrate  --noinput
supervisord
python manage.py collectstatic --no-input
echo "Server will be started!"
gunicorn --config gunicorn_config.py grc.wsgi:application
