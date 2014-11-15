#!/bin/sh
mysql -u root -pL33che$ -e 'drop database Blazon;'
mysql -u root -pL33che$ -e 'create database Blazon;'
rm -f sponsorship/migrations/0*
python manage.py makemigrations
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@blazon.com', 'blazon')" | python manage.py shell
echo "\n"