#!/usr/bin/env bash
# exit on error
set -o errexit

# Install system dependencies
sudo apt-get update
sudo apt-get install -y libssl-dev

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py makemigrations