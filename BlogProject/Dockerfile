FROM python:3.12.2-slim-bullseye

WORKDIR /usr/src/BlogProject

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat cron && touch /var/log/cron.log

RUN pip install --upgrade pip
COPY ./requirements.txt .
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./entrypoint.sh /usr/src/BlogProject/entrypoint.sh
RUN chmod +x /usr/src/BlogProject/entrypoint.sh

COPY ./blog-cron.py /usr/src/BlogProject/blog-cron.py
RUN chmod +x /usr/src/BlogProject/blog-cron.py

COPY ./flush_tokens.sh /usr/src/BlogProject/flush_tokens.sh
RUN chmod +x /usr/src/BlogProject/flush_tokens.sh

# COPY ./cronjob /etc/cron.d/crontab 
# RUN chmod 0644 /etc/cron.d/crontab



# RUN (crontab -l ; echo "*/1 * * * * /usr/local/bin/python3 /usr/src/BlogProject/blog-cron.py >> /var/log/cron.log 2>&1") | crontab

RUN echo "*/1 * * * * /usr/local/bin/python /usr/src/BlogProject/blog-cron.py >> /var/log/cron.log 2>&1" | crontab -


ENTRYPOINT ["/usr/src/BlogProject/entrypoint.sh"]
CMD ["python", "manage.py", "runserver"]
# CMD ["./manage.py", "runserver", "0.0.0.0:8080"]