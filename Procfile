web: daphne lechat.asgi:application --port $PORT --bind 0.0.0.0 -v2
release: python manage.py migrate
worker: python manage.py runworker channels --settings=lechat.settings -v2
