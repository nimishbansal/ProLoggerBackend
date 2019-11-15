import socket

from django.core.management.commands.runserver import Command as RunCommand

from socketio_app.views import sio
import os
import time


class Command(RunCommand):
    help = 'Run the Socket.IO server'

    def handle(self, *args, **options):
        if sio.async_mode == 'threading':
            super(Command, self).handle(*args, **options)
        elif sio.async_mode == 'eventlet':
            import eventlet
            import eventlet.wsgi
            from ProLogger.wsgi import socket_application
            import threading

            def fun():
                print(os.system("sudo kill -9 `sudo lsof -t -i:5000`"))
                time.sleep(4)
                eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), socket_application)

            t = threading.Thread(target=fun)
            t.start()
            super(Command, self).handle(*args, **options)
