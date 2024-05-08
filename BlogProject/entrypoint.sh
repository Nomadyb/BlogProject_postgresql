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


# // This part of the shell script is checking if the first argument passed to the script is "cron". If
# // the condition is true, it will start the cron service, display the current cron jobs for the Django
# // project using `python manage.py crontab show`, install the cron jobs from `/etc/cron.d/crontab`
# // using `crontab`, start the cron daemon using `cron`, and then continuously display the log output of
# // the cron service using `tail -f /var/log/cron.log`.

if [ "$1" = "cron" ]; then
  echo "Starting cron service..."
  service cron start
  python manage.py crontab show
  crontab /etc/cron.d/crontab
  cron && tail -f /var/log/cron.log
fi

# Execute any additional commands passed to the script
exec "$@"
