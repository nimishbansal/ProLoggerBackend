import os

# Create your views here.
import socketio

sio = socketio.Server(async_mode='eventlet')


@sio.event
def connect(sid, environ):
    print('connected to ', sid)
    return True


@sio.event
def disconnect(sid):
    print("disconnected", sid)


@sio.on('chat')
def on_message(sid, data):
    print('I received a message!', data, "with pid=", os.getpid())
    sio.emit("chat", "received your msg" + str(data))
    sio.emit("chat", "welcome")
