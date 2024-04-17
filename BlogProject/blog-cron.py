# cron_job.py

import os
import sys
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    # Django yönetim komutunu çalıştır
    execute_from_command_line(['manage.py', 'flushexpiredtokens'])
