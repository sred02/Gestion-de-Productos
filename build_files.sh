#!/bin/bash
set -e

pip install --break-system-packages -r requirements.txt

cd uniweb2
python manage.py collectstatic --noinput
python manage.py migrate --noinput
