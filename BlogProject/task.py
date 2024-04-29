import logging
import os

from celery import Celery
from celery.schedules import crontab

from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BlogProject.settings")

app = Celery("BlogProject", broker_connection_retry_on_startup=True)
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.worker_hijack_root_logger = False

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

logger = logging.getLogger(__name__)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(), flush_expired_tokens.s(),
    )


@app.task
def flush_expired_tokens():
    call_command("flushexpiredtokens")
    logger.info("Expired JWT refresh tokens flushed.")
