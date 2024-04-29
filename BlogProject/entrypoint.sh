#!/bin/sh

# Check if the database is PostgreSQL and wait until it's ready
if [ "$DATABASE" = "postgres" ]; then
    echo "Checking if the database is running..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "The database is up and running :-)"
fi

# Run Django migrations
python manage.py makemigrations
python manage.py migrate

# If this is going to be a cron container, set up the crontab.
if [ "$1" = "cron" ]; then
  echo "Starting cron service..."
  service cron start
  python manage.py crontab show
  crontab /etc/cron.d/crontab
  cron && tail -f /var/log/cron.log
fi

# Execute any additional commands passed to the script
exec "$@"