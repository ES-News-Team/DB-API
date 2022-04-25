import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import select
import uuid

# Define the MariaDB engine using MariaDB Connector/Python
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:1234567890@mariadb:3306/esnews")

Base = declarative_base()



class User(Base):
   __tablename__ = 'users'
   id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
   name = sqlalchemy.Column(sqlalchemy.String(length=100))
   email = sqlalchemy.Column(sqlalchemy.String(length=100))
   password = sqlalchemy.Column(sqlalchemy.String(length=100))
   active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()



def addUser(name, email, password):

   newUser = User(name=name, email=email, password=password)
   session.add(newUser)
   session.commit()

def selectAll():
   users = session.query(User).all()
   
def getEmail(email):
   stmt = select(User).where(User.email == email)
   user = session.scalars(stmt).one()
   return user
   
   

def selectByStatus(isActive):
   users = session.query(User).filter_by(active=isActive)

def updateUserStatus(id, isActive):
   user = session.query(User).get(id)
   user.active = isActive
   session.commit()

def deleteUser(id):
   session.query(User).filter(User.id == id).delete()
   session.commit()
