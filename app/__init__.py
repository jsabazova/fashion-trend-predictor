# app/__init__.py

from flask import Flask

app = Flask(__name__)

# Initialize app configurations
app.config.from_pyfile('config.py')

from app import routes
