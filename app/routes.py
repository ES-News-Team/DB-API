from flask import request
from models.users import *
from app import db_api
import bcrypt


@db_api.route('/')
def index():
    return 'Hello :)'



@db_api.route('/register', methods=['POST'])
def register():
  data = request.get_json()
  password = data['password'].encode('utf-8')
  hashed = bcrypt.hashpw(password, bcrypt.gensalt())
  addUser(data['name'], data['email'], hashed)

  
  return {
    "name": data['name'],
    "email": data['email']
  }

@db_api.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  password = data['password']

  user = getEmail(data['email'])

  if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
    return f'Welcome {user.name}', 200
  else:
    return 'Wrong password', 403
  