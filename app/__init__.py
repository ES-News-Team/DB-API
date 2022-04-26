from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api

db_api = Flask(__name__)
api = Api(db_api)
Bcrypt(db_api) # see it later...

from app.routes import *
