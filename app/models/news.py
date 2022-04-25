import sqlalchemy
import uuid
from app.models.Base import BASE, ENGINE, SESSION

def generateID():
  return str(uuid.uuid4())

class News(BASE):
   __tablename__ = 'news'
   uuid = sqlalchemy.Column(sqlalchemy.String(length=36), name= "uuid", primary_key=True, default=generateID)
   title = sqlalchemy.Column(sqlalchemy.String(length=100))
   image = sqlalchemy.Column(sqlalchemy.String(length=300))
   content = sqlalchemy.Column(sqlalchemy.Text)

BASE.metadata.create_all(ENGINE)
