from flask_socketio import SocketIO
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'no'
socketapp = SocketIO(app)

from chat.routes import *