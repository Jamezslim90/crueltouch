#!/usr/bin/env bash
# exit on error
set -o errexit

# Show commands being executed
set -x

# Force reinstall Django and dependencies
echo "Reinstalling Django and dependencies..."
pip uninstall -y django django-js-asset django-simple-history django-simple-captcha
pip install --no-cache-dir Django==4.2.8
pip install --no-cache-dir -r requirements.txt

# Clean up existing static files
rm -rf staticfiles/*

# Remove all existing migrations
echo "Removing existing migrations..."
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

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

# Show directory structure before migrations
echo "Directory structure before migrations:"
ls -la */migrations/

# Create migrations for auth and contenttypes first
echo "Creating migrations for core apps..."
python manage.py makemigrations auth contenttypes --verbosity 3

# Create migrations for client app
echo "Creating migrations for client app..."
python manage.py makemigrations client --verbosity 3

# Create remaining migrations
echo "Creating remaining migrations..."
python manage.py makemigrations --verbosity 3

# Show directory structure after migrations
echo "Directory structure after migrations:"
ls -la */migrations/

# Run collectstatic
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Show current migration status
echo "Current migration status:"
python manage.py showmigrations

# Apply migrations in order
echo "Applying migrations..."
python manage.py migrate auth --verbosity 3
python manage.py migrate contenttypes --verbosity 3
python manage.py migrate client --verbosity 3
python manage.py migrate --verbosity 3

# Show final migration status
echo "Final migration status:"
python manage.py showmigrations