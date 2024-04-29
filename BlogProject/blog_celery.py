# blog_celery.py

import os
import subprocess
from celery import Celery
from celery.schedules import crontab

# Django ayarlarını yükle
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BlogProject.settings')

app = Celery('blog_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute=0, hour=0),
                             remove_expired_tokens_from_db.s(),
                             name='remove_expired_tokens_from_db')


@app.task
def remove_expired_tokens_from_db():
    subprocess.run(['python', 'manage.py', 'flushexpiredtokens'])
