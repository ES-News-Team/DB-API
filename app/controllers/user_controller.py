from app.controllers.controller_interface import IUserController
from app.models.base import SESSION
from app.models.users import User
from sqlalchemy import select


class UserController(IUserController):

    def retrieve(self, email: str):
        stmt = select(User).where(User.email == email)
        try:
            user = SESSION.scalars(stmt).one()
            return user
        except:
            SESSION.rollback()


    def create(self, name: str, email: str, password: str):
        exists = SESSION.query(User.email).filter_by(email=email).first() 
        if exists:
            return 409
        else:
            newUser = User(name=name, email=email, password=password)
            SESSION.add(newUser)
            SESSION.commit()
            return newUser
       
