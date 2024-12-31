#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Clean up existing static files
rm -rf staticfiles/*

# Ensure migrations directories exist
echo "Creating migrations directories..."
mkdir -p client/migrations
mkdir -p administration/migrations
mkdir -p homepage/migrations
mkdir -p portfolio/migrations
mkdir -p static_pages_and_forms/migrations
mkdir -p appointment/migrations
mkdir -p payment/migrations

# Create __init__.py in migrations directories
touch client/migrations/__init__.py
touch administration/migrations/__init__.py
touch homepage/migrations/__init__.py
touch portfolio/migrations/__init__.py
touch static_pages_and_forms/migrations/__init__.py
touch appointment/migrations/__init__.py
touch payment/migrations/__init__.py

# First, create all migrations
echo "Creating migrations..."
python manage.py makemigrations client --no-input
python manage.py makemigrations administration --no-input
python manage.py makemigrations homepage --no-input
python manage.py makemigrations portfolio --no-input
python manage.py makemigrations static_pages_and_forms --no-input
python manage.py makemigrations appointment --no-input
python manage.py makemigrations payment --no-input

# Run collectstatic
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Apply migrations
echo "Applying migrations..."
python manage.py migrate --no-input

# Show migration status
python manage.py showmigrations