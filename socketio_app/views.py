from django.shortcuts import render

# Create your views here.
import socketio
sio = socketio.Server(async_mode='eventlet', always_connect=True)

@sio.event
def connect(sid, environ):
    print('connected to ', sid)
    return True

#@sio.event
#def my_message(sid, data):
#    print('message ', data)

@sio.event
def disconnect(sid):
    print("disconnected", sid)

@sio.on('chat')
def on_message(sid, data):
    print('I received a message!', data)
    sio.emit("chat", "received your msg"+str(data))
