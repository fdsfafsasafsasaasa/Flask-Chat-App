from flask_socketio import SocketIO, send, emit
from flask import Flask, render_template
from chat import socketapp, app
from datetime import datetime

messages = []

@app.route("/")
def root(data=None):
    return render_template("index.html", messages=messages)

@socketapp.on('message_send')
def message_send(message):
    messages.append(message)
    emit("message_recv", message, broadcast=True)
