from flask import Flask
from pymongo import MongoClient

app = Flask(__name__, template_folder='../templates')  # Specify the template folder

# Configure MongoDB client
client = MongoClient('mongodb://localhost:27017/')
db = client.github_webhooks

from app import routes
