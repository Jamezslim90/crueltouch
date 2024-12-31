#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Clean up existing static files
rm -rf staticfiles/*

# Ensure the database is clean and migrations are in sync
python manage.py migrate --fake-initial
python manage.py migrate auth zero
python manage.py migrate contenttypes zero
python manage.py migrate admin zero
python manage.py migrate sessions zero
python manage.py migrate sites zero

# Create migrations for all apps
python manage.py makemigrations administration
python manage.py makemigrations client
python manage.py makemigrations homepage
python manage.py makemigrations portfolio
python manage.py makemigrations static_pages_and_forms
python manage.py makemigrations appointment
python manage.py makemigrations payment

# Run collectstatic
python manage.py collectstatic --no-input

# Apply migrations
python manage.py migrate --fake-initial
python manage.py migrate