#!/usr/bin/env bash
set -o errexit

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Set Django settings module
export DJANGO_SETTINGS_MODULE=baitulhikmah.settings

# Run Django commands
python3 manage.py collectstatic --no-input
python3 manage.py migrate