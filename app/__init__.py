from flask import Flask

db_api = Flask(__name__)

import app.routes
