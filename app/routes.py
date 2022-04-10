from flask import request
from models.users import *
from models.news import *
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


@db_api.route('/news/', methods=['POST'])
def insertNews():
  data = request.get_json()
  addNews(data['title'], data['image'], data['content'])

  
  return 'News created', 201

@db_api.route('/news/', methods=['PUT'])
def update():
  data = request.get_json()
  updateNews(data['id'], data['title'], data['image'], data['content'])

  
  return 'News updated', 200

@db_api.route('/news/', methods=['DELETE'])
def delete():
  data = request.get_json()
  deleteNews(data['id'])

  
  return 'News Deleted', 200

@db_api.route('/news/', methods=['GET'])
def read():
  data = request.get_json()
  response = readNews(data['id'])

  obj = {
    "id": response.uuid,
    "title": response.title,
    "image": response.image,
    "content": response.content 
  }
  
  return obj, 200