import logging
import sys
from logging import Handler, getLevelName
import requests
from raven.contrib.django.handlers import SentryHandler

requests.get("https://google.co.in")

# /home/nimish/PycharmProjects/ProLoggerBackend/ProLogger/venv/lib/python3.6/site-packages/raven/base.py:731
def get_dj_logger():
    return logging.getLogger('sentry_debug_logger')


class DjLogHandler(Handler):
    """
    A handler class which writes logging records, appropriately formatted,
    to somewhere.
    """

    terminator = '\n'

    def __init__(self, stream=None):
        """
        Initialize the handler.

        If stream is not specified, sys.stderr is used.
        """
        print("hmmou")
        Handler.__init__(self)
        if stream is None:
            stream = sys.stderr
        self.stream = stream

    def flush(self):
        """
        Flushes the stream.
        """
        self.acquire()
        try:
            if self.stream and hasattr(self.stream, "flush"):
                self.stream.flush()
        finally:
            self.release()

    # noinspection PyBroadException
    def emit(self, record):
        """
        Emit a record.

        If a formatter is specified, it is used to format the record.
        The record is then written to the stream with a trailing newline.  If
        exception information is present, it is formatted using
        traceback.print_exception and appended to the stream.  If the stream
        has an 'encoding' attribute, it is used to determine how to do the
        output to the stream.
        """
        print("record is ", record)
        try:
            msg = self.format(record)
            print("message is", msg, 'with length', len(msg))
            stream = self.stream
            stream.write(msg)
            stream.write(self.terminator)
            self.flush()
        except Exception:
            self.handleError(record)

    def __repr__(self):
        level = getLevelName(self.level)
        name = getattr(self.stream, 'name', '')
        if name:
            name += ' '
        return '<%s %s(%s)>' % (self.__class__.__name__, name, level)
