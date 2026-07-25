#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Set Django settings module
export DJANGO_SETTINGS_MODULE=baitulhikmah.settings

# Run Django commands
python manage.py collectstatic --no-input --settings=baitulhikmah.settings
python manage.py migrate --settings=baitulhikmah.settings