# Initalizes the api module
from flask import Flask
app = Flask(__name__)
app.config.from_pyfile("config/config.py")

import agora_api.routes