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

def new_log_entry_emit_thread(data):
    sio.emit('chat',data)

def send_new_log_entry_event(data):
    sio.start_background_task(target=new_log_entry_emit_thread, data=data)
