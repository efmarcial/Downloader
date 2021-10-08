web: gunicorn ytmp.wsgi --log-file - --log-level debug
web: python manage.py runserver
python manage.py collectstatic --noinput
manage.py migrate