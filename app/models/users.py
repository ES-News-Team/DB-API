import sqlalchemy
from app.models.base import BASE, ENGINE
from utils.generate_id import generateID

class User(BASE):
   __tablename__ = 'users'
   id = sqlalchemy.Column(sqlalchemy.String(length=36), name= "id", primary_key=True, default=generateID)
   name = sqlalchemy.Column(sqlalchemy.String(length=100))
   email = sqlalchemy.Column(sqlalchemy.String(length=100))
   password = sqlalchemy.Column(sqlalchemy.String(length=100))
   active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

BASE.metadata.create_all(ENGINE)
