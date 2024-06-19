from app import db
from datetime import datetime

class MongoDB:
    @staticmethod
    def insert_event(event):
        db.events.insert_one(event)

    @staticmethod
    def get_latest_events(limit=10):
        events = list(db.events.find().sort('timestamp', -1).limit(limit))
        for event in events:
            event['_id'] = str(event['_id'])
        return events

class GitHubEventHandler:
    @staticmethod
    def handle_event(data):
        print(data)
        event = {
            'request_id': '',
            'author': '',
            'action': '',
            'from_branch': '',
            'to_branch': '',
            'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        }

        if 'pusher' in data:
            print("##Push Request##")
            event['request_id'] = data['head_commit']['id']
            event['author'] = data['pusher']['name']
            event['action'] = 'PUSH'
            event['to_branch'] = data['ref'].split('/')[-1]

        elif 'pull_request' in data and data['action'] !='closed':
            print("##Pull Request##")
            event['request_id'] = data['pull_request']['id']
            event['author'] = data['pull_request']['user']['login']
            event['action'] = 'PULL_REQUEST'
            event['from_branch'] = data['pull_request']['head']['ref']
            event['to_branch'] = data['pull_request']['base']['ref']

        elif 'action' in data and data['action'] == 'closed' and data['pull_request']['merged']:
            event['request_id'] = data['pull_request']['id']
            event['author'] = data['pull_request']['user']['login']
            event['action'] = 'MERGE'
            event['from_branch'] = data['pull_request']['head']['ref']
            event['to_branch'] = data['pull_request']['base']['ref']

        return event
