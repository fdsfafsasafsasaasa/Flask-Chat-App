from flask_socketio import SocketIO, send, emit
from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'no'
socketapp = SocketIO(app)
messages = []
@app.route("/")
def root(data=None):
    return render_template("index.html", messages=messages)

@socketapp.on('message_send')
def message_send(message):
    messages.append(message)
    print(f"Message sent from: {message['user']}\nMessage content: {message['body']}\nMessage time: {message['date']}")
    emit("message_recv", message, broadcast=True)
if __name__ == '__main__':
    socketapp.run(app)