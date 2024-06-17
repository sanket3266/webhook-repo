from flask import request, jsonify, render_template
from app import app, db
from app.models import GitHubEventHandler, MongoDB
from datetime import datetime

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        event = GitHubEventHandler.handle_event(data)
        
        if event['action']:
            MongoDB.insert_event(event)
            return jsonify({'message': 'Event received'}), 200
        else:
            return jsonify({'message': 'Unhandled event'}), 400

    return jsonify({'message': 'Invalid request'}), 400


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/events', methods=['GET'])
def get_events():
    events = MongoDB.get_latest_events()
    return jsonify(events)
