from flask import Flask, render_template,request
from flask_socketio import SocketIO,emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
uu= ""
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('index.html', username=username)

    else:
        return render_template('landing.html')



@socketio.on('my event')
def handle_message(message):
    emit('message_receive',message,broadcast=True)

@socketio.on('disconnect1')
def handle_message1(message):
    print message
    socketio.emit('dc', message)

@socketio.on('connect1')
def handle_message2(message):
    socketio.emit('c',message)

@socketio.on('keydown')
def handle_message3(message):
    socketio.emit('kd',message)

@socketio.on('keyup')
def handle_message4(message):
    socketio.emit('ku',message)

if __name__ == '__main__':
    socketio.run(app,debug=True)


