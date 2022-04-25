from app.controllers.controller_interface import IUserController
from app.models.base import SESSION
from app.models.users import User
from sqlalchemy import select


class UserController(IUserController):

    def retrieve(self, email: str):
        stmt = select(User).where(User.email == email)
        user = SESSION.scalars(stmt).one()
        return user


    def create(self, name: str, email: str, password: str):
        newUser = User(name=name, email=email, password=password)
        SESSION.add(newUser)
        SESSION.commit()
