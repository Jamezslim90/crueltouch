#!/usr/bin/env bash
# exit on error
set -o errexit

# Show commands being executed
set -x

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

# Create __init__.py in migrations directories if they don't exist
for dir in */migrations/; do
    if [ ! -f "${dir}__init__.py" ]; then
        touch "${dir}__init__.py"
        echo "Created ${dir}__init__.py"
    fi
done

# First, create all migrations with verbosity
echo "Creating migrations..."
python manage.py makemigrations client --verbosity 3
python manage.py makemigrations administration --verbosity 3
python manage.py makemigrations homepage --verbosity 3
python manage.py makemigrations portfolio --verbosity 3
python manage.py makemigrations static_pages_and_forms --verbosity 3
python manage.py makemigrations appointment --verbosity 3
python manage.py makemigrations payment --verbosity 3

# Run collectstatic
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Show current migration status
echo "Current migration status:"
python manage.py showmigrations

# Apply migrations with verbosity
echo "Applying migrations..."
python manage.py migrate --verbosity 3

# Show final migration status
echo "Final migration status:"
python manage.py showmigrations