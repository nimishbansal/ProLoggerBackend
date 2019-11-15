from django.core.management.commands.runserver import Command as RunCommand

from socketio_app.views import sio
import os


class Command(RunCommand):
    help = 'Run the Socket.IO server'

    def handle(self, *args, **options):
        if sio.async_mode == 'threading':
            super(Command, self).handle(*args, **options)
        elif sio.async_mode == 'eventlet':
            import eventlet
            import eventlet.wsgi
            from ProLogger.wsgi import application
            import threading
            def fun():
                print(os.system("sudo kill -9 `sudo lsof -t -i:5000`"))
                eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), application)
            t = threading.Thread(target=fun)
            t.start()
            import time
            time.sleep(3.5)

            super(Command, self).handle(*args, **options)
