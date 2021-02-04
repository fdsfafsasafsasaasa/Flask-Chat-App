from flask_socketio import SocketIO
from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'no'
socketapp = SocketIO(app)

@app.route("/")
def root(data=None):
    return render_template("index.html")

@socketapp.on('message_send')
def message_send(message):
    print(f"Message sent from: {message['user']}\nMessage content: {message['body']}\nMessage time: {datetime.now()}")

if __name__ == '__main__':
    socketapp.run(app)