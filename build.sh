#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Clean up existing static files
rm -rf staticfiles/*

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py makemigrations