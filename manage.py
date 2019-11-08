#!/usr/bin/env python
import os
import sys
import _thread as thread

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProLogger.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    if sys.argv.__contains__('runserver'):
        print(os.system('sudo kill -9 `sudo lsof -t -i:6379`'))
        print(thread.start_new_thread(os.system, ('celery -A ProLogger worker -l info',)))
        # print(os.spawnlp(os.P_NOWAIT, 'celery -A ProLogger worker -l info'))

    execute_from_command_line(sys.argv)
