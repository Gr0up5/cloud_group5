#!/bin/bash
DB_NAME=tiramisu
createdb $DB_NAME
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('carlos', 'admin@mail.com', 'carlos')" | ./manage.py shell