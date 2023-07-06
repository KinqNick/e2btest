from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from game_logic import GameState, update_game

app = Flask(__name__)
socketio = SocketIO(app)

game_state = GameState()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('keydown')
def handle_keydown_event(key):
    global game_state
    game_state = update_game(game_state, key)
    emit('game_update', game_state, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)