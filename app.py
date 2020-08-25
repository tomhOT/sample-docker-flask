from flask import Flask, request, jsonify
from os import listdir, getenv
from datetime import datetime

directory = getenv('STORAGE_DIR') or '/app/messages'
app = Flask(__name__)

# :)
@app.route('/')
def hello_world():
    return 'Hello, World!\n'

# Ping pong
@app.route('/echo', methods=['POST'])
def echo():
    return f'right back at ya: {request.get_data().decode("utf-8")}\n'

# Create or retrieve messages based on request method
@app.route('/message/<title>', methods=['GET', 'POST'])
def message(title):
    if request.method == 'GET':
        with open(f'{directory}/{title}', 'r') as msg:
            return jsonify({'title': title, 'message': msg.read()})

    elif request.method == 'POST':
        with open(f'{directory}/{title}', 'w') as msg:
            msg.write(request.get_data().decode('utf-8'))

        return jsonify(success=True)

# List all messages in storage
@app.route('/messages', methods=['GET'])
def messages():
    message_titles = listdir(directory)
    body = { 'data': { 'items': message_titles } }

    return jsonify(body)
