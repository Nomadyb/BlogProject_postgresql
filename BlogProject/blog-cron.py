#!/usr/local/bin/python


# from django.core.management.base import BaseCommand
# from django.core.management import call_command
# from datetime import datetime


# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         call_command('flushexpiredtokens')
#         print("flushexpiredtokens command executed successfully at", datetime.now())

# import subprocess
# from datetime import datetime


# def flush_expired_tokens():
#     result = subprocess.check_output(
#         ['/usr/local/bin/python', 'manage.py', 'flushexpiredtokens'])
#     print(result.decode("utf-8"))
#     print("flushexpiredtokens command executed successfully at", datetime.now())

# if __name__ == "__main__":
#     flush_expired_tokens()


from django.core.management.base import BaseCommand
from django.core.management import call_command
from datetime import timedelta, date, datetime


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command('flushexpiredtokens')
        print("flushexpiredtokens command executed successfully at", datetime.now())



"""
bu ilk
"""
#!/usr/local/bin/python
# from datetime import timedelta, date, datetime
# from django.core.management import call_command
# from django.core.management.base import BaseCommand
# import os
# import sys
# import django

# # path to your project if needed
# sys.path.append('/usr/src/BlogProject')
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BlogProject.settings")
# django.setup()


# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         call_command('flushexpiredtokens')
#         print("flushexpiredtokens command executed successfully at", datetime.now())






# import logging
# from django.core import management

# logger = logging.getLogger(__name__)


# def flush_expired_tokens():
#     """
#     flushes all expired tokens from OutstandingToken and BlacklistedToken models.
#     """
#     logger.info("started flush_expired_tokens")
#     management.call_command("flushexpiredtokens")
#     logger.info("finished flush_expired_tokens")


# import subprocess
# import sys
# from django.core.management import call_command


# def remove_expired_tokens_from_db():
#     call_command("flushexpiredtokens")


# if __name__ == "__main__":
#     remove_expired_tokens_from_db()




# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         call_command('python', 'manage.py', 'flushexpiredtokens')
#         print("flushexpiredtokens command executed successfully at", datetime.now())
        
# from django.core.management.base import BaseCommand
# from datetime import datetime
# from ...models import OutstandingToken


# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         OutstandingToken.objects.filter(
#             expires_at__lte=datetime.now()).delete()
#         print("flushexpired command executed successfully at", datetime.now())


# from django.core.management.base import BaseCommand
# from datetime import datetime
# from ...models import OutstandingToken


# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         # Expired tokensi silme işlemi
#         OutstandingToken.objects.filter(
#             expires_at__lte=datetime.now()).delete()

#         # Log mesajı yazdırma
#         self.stdout.write(self.style.SUCCESS(
#             'Expired tokens successfully flushed at {}'.format(datetime.now())))
