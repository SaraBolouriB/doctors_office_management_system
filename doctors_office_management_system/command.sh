#!/bin/bash

python manage.py makemigrations user_account
python manage.py migrate
python manage.py runserver 0.0.0.0:8000