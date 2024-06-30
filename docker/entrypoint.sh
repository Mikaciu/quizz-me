#!/bin/bash

echo "Executing migrations ..."
python manage.py migrate

echo "Applying fixtures ..."
python manage.py loaddata initial_data

echo "Running server ..."
python manage.py runserver 0.0.0.0:8000
