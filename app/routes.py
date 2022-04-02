from flask import request
from models.users import *
from app import db_api


@db_api.route('/')
def index():
    return 'Hello :)'



@db_api.route('/register', methods=['POST'])
def register():
  data = request.get_json()
 

  addUser(data['name'],data['lastname'])

  
  return {
    "name": data['name'],
    "lastname": data['lastname']
  }
  