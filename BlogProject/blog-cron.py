# cron_job.py

# import os
# import sys
# from django.core.management import execute_from_command_line

# if __name__ == "__main__":
#     # Django yönetim komutunu çalıştır
#     execute_from_command_line(['manage.py', 'flushexpiredtokens'])


from django.core.management.base import BaseCommand
from django.core.management import call_command
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command('flushexpired')
        print("flushexpired command executed successfully at", datetime.now())
