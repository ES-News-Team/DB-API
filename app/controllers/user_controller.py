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
        newUser = User(name=name, email=email, password=password)
        try:
            SESSION.add(newUser)
            SESSION.commit()
        except:
            SESSION.rollback()
