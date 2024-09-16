from flask import Flask
from flask_pymongo import PyMongo
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('app.config.Config')

mongo = PyMongo(app)
ma = Marshmallow(app)

from app import routes
