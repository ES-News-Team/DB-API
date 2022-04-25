from flask import Flask

db_api = Flask(__name__)

Bcrypt(db_api) # see it later...

import app.routes
