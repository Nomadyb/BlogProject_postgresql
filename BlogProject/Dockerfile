FROM python:3.12.2-slim-bullseye
WORKDIR /usr/src/BlogProject


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat
RUN apt-get update && apt-get install -y cron && touch /var/log/cron.log


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN (crontab -l ; echo "* * * * * echo "cron task is working!" >> /var/log/cron.log") | crontab -
CMD cron && tail -f /var/log/cron.log

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/BlogProject/entrypoint.sh
RUN chmod +x /usr/src/BlogProject/entrypoint.sh

COPY . .


# Crontab copy 
COPY ./blog-cron.py /usr/src/BlogProject/blog-cron.py

# Crontab script permission
RUN chmod +x /usr/src/BlogProject/blog-cron.py

# RUN service cron start

ENTRYPOINT [ "/usr/src/BlogProject/entrypoint.sh" ]


