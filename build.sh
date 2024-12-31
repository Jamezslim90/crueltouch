#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Clean up existing static files
rm -rf staticfiles/*

# First, create all migrations
echo "Creating migrations..."
python manage.py makemigrations client  # Custom user model first
python manage.py makemigrations administration
python manage.py makemigrations homepage
python manage.py makemigrations portfolio
python manage.py makemigrations static_pages_and_forms
python manage.py makemigrations appointment
python manage.py makemigrations payment

# Run collectstatic
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Apply migrations in specific order
echo "Applying migrations..."

# First, apply contenttypes and auth
python manage.py migrate contenttypes --fake-initial
python manage.py migrate auth --fake-initial

# Apply client app migrations one by one to handle dependencies
for migration in $(ls client/migrations/0*.py | sort -V); do
    migration_name=$(basename "$migration" .py)
    echo "Applying client migration: $migration_name"
    python manage.py migrate client "${migration_name#*_}" --fake-initial
done

# Apply remaining core apps
python manage.py migrate admin --fake-initial
python manage.py migrate sessions --fake-initial
python manage.py migrate sites --fake-initial

# Apply third-party apps
python manage.py migrate captcha --fake-initial
python manage.py migrate django_q --fake-initial

# Apply remaining apps
python manage.py migrate administration --fake-initial
python manage.py migrate homepage --fake-initial
python manage.py migrate portfolio --fake-initial
python manage.py migrate static_pages_and_forms --fake-initial
python manage.py migrate appointment --fake-initial
python manage.py migrate payment --fake-initial

# Final migration to catch any remaining dependencies
echo "Running final migration check..."
python manage.py migrate --fake-initial