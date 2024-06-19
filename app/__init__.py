from flask import Flask
from pymongo import MongoClient
from config import Config

app = Flask(__name__, template_folder='../templates')
app.config.from_object(Config)

# Configure MongoDB client
client = MongoClient(app.config['MONGO_URI'])
db = client.github_webhooks

from app import routes
