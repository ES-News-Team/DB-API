from email.policy import default
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select
import uuid

# Define the MariaDB engine using MariaDB Connector/Python
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:1234567890@mariadb:3306/esnews")

Base = declarative_base()

def generateID():
  return str(uuid.uuid4())

class News(Base):
   __tablename__ = 'news'
   uuid = sqlalchemy.Column(sqlalchemy.String(length=100), name= "uuid", primary_key=True, default=generateID)
   title = sqlalchemy.Column(sqlalchemy.String(length=100))
   image = sqlalchemy.Column(sqlalchemy.String(length=100))
   content = sqlalchemy.Column(sqlalchemy.Text)

Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

def addNews(title, image, content):

   newNews = News(title=title, image=image, content=content)
   session.add(newNews)
   session.commit()

def deleteNews(id):
   session.query(News).filter(News.uuid == id).delete()
   session.commit()

def updateNews(id, title, image, content):
   news = session.query(News).get(id)
   news.title = title
   news.image = image
   news.content = content
   session.commit()

def readNews(id):
  stmt = select(News).where(News.uuid == id)
  news = session.scalars(stmt).one()
  
  return news