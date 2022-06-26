#!/bin/sh

set -e

exec python manage.py runserver 0.0.0.0:8000 &
exec python ra83.py