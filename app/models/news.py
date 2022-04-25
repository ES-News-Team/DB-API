import sqlalchemy
from utils.generate_id import generateID
from app.models.base import BASE, ENGINE

class News(BASE):
   __tablename__ = 'news'
   id = sqlalchemy.Column(sqlalchemy.String(length=36), name= "id", primary_key=True, default=generateID)
   title = sqlalchemy.Column(sqlalchemy.String(length=100))
   image = sqlalchemy.Column(sqlalchemy.String(length=300))
   content = sqlalchemy.Column(sqlalchemy.Text)

BASE.metadata.create_all(ENGINE)
