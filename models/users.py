import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

# Define the MariaDB engine using MariaDB Connector/Python
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:sysadm@127.0.0.1:3306/esnews")

Base = declarative_base()

class User(Base):
   __tablename__ = 'users'
   id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
   firstname = sqlalchemy.Column(sqlalchemy.String(length=100))
   lastname = sqlalchemy.Column(sqlalchemy.String(length=100))
   active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

def addUser(firstName,lastName):
   newUser = User(firstname=firstName, lastname=lastName)
   session.add(newUser)
   session.commit()

def selectAll():
   users = session.query(User).all()
   

def selectByStatus(isActive):
   users = session.query(User).filter_by(active=isActive)

def updateUserStatus(id, isActive):
   user = session.query(User).get(id)
   user.active = isActive
   session.commit()

def deleteUser(id):
   session.query(User).filter(User.id == id).delete()
   session.commit()

# # # Add some new employees
# addEmployee("Bruce", "Wayne")
# addEmployee("Diana", "Prince")
# addEmployee("Clark", "Kent")

# # Show all employees
# print('All Employees')
# selectAll()
# print("----------------")

# # Update employee status
# updateEmployeeStatus(2,False)

# # Show active employees
# print('Active Employees')
# selectByStatus(True)
# print("----------------")

# # Delete employee
# deleteEmployee(1)

# # Show all employees
# print('All Employees')
# selectAll()
# print("----------------")