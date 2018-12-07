"""Flask-based application initialization and configuration."""

from flask import Flask

app = Flask(__name__)
app.config.from_object('server.config')
