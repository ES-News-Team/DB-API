import bcrypt
from app import db_api
from flask import request
from app.controllers.user_controller import UserController

USER = UserController()

@db_api.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    password = data['password'].encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    response = USER.create(data['name'], data['email'], hashed)

    if response == 409:
        return 'Email already exists', 409
    else:
        return {
            "name": response.name,
            "email": response.email
            
        }, 201

@db_api.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()

    password = data['password']
    user = USER.retrieve(data['email'])

    if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return f'Welcome {user.name}', 200
    else:
        return 'Wrong password', 403