#!/usr/bin/env bash
# exit on error
set -o errexit

# Show commands being executed
set -x

# Clean up virtual environment
echo "Cleaning up virtual environment..."
rm -rf .venv
python -m venv .venv
source .venv/bin/activate

# Install requirements
echo "Installing requirements..."
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

# Create all migrations at once
echo "Creating migrations for all apps..."
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

# Try to run migrations with --run-syncdb first
echo "Running initial syncdb..."
python manage.py migrate --run-syncdb

# Apply migrations with verbosity
echo "Applying migrations..."
python manage.py migrate --verbosity 3

# Show final migration status
echo "Final migration status:"
python manage.py showmigrations