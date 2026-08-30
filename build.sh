#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations core --no-input
python manage.py migrate --no-input

# Collect static files
python manage.py collectstatic --no-input