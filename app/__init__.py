from flask import Flask
from flask_bcrypt import Bcrypt

db_api = Flask(__name__)

Bcrypt(db_api) # see it later...

from app.routes import *
