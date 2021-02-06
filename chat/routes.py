from flask_socketio import SocketIO, send, emit
from flask import Flask, render_template
from chat import socketapp, app
from datetime import datetime
import sqlite3

conn = sqlite3.connect("messages.db")
c = conn.cursor()

@app.route("/")
def root(data=None):    
    return render_template("index.html", messages=c.execute("SELECT * FROM messages").fetchall())

@socketapp.on('message_send')
def message_send(message):
    print(c.execute("SELECT * FROM messages").fetchall())
    c.execute("INSERT INTO messages VALUES (?, ?)", (message['user'], message['body']))
    conn.commit()
    emit("message_recv", message, broadcast=True)
