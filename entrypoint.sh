#!/bin/sh
set -e

echo "Apply migrations..."
python manage.py makemigrations
python manage.py migrate --noinput

echo "Create superuser (if not exists)..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
email = "$DJANGO_SUPERUSER_EMAIL"
password = "$DJANGO_SUPERUSER_PASSWORD"
if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(email=email, password=password)
EOF

echo "Mount static files..."
python manage.py collectstatic --noinput

echo "Run app..."
exec python manage.py runserver 0.0.0.0:8000
