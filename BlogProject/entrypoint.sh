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



# Add crontab jobs
python manage.py crontab add
python manage.py crontab show

# Execute any additional commands passed to the script
exec "$@"
