#!/bin/sh
set -e

if [ "$DB_HOST" ]; then
  echo "Waiting for PostgreSQL at $DB_HOST:$DB_PORT..."
  until nc -z "$DB_HOST" "$DB_PORT"; do
    sleep 1
  done
fi

python manage.py collectstatic --noinput || true

exec "$@"
