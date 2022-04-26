from app.models.base import SESSION
from app.models.news import News
from sqlalchemy import select
from app.controllers.controller_interface import IController
from app.models.base import SESSION
class NewsController(IController):
       
    def list(self):
       return SESSION.query(News).all()

    
    def retrieve(self, id: str):
        stmt = select(News).where(News.id == id)
        news = SESSION.scalars(stmt).one()
        return news
      

    def create(self, title, image, content):  
        newNews = News(title=title, image=image, content=content)
        SESSION.add(newNews)
        SESSION.commit()


    def update(self, id, title, image, content):
        news = SESSION.query(News).get(id)
        news.title = title
        news.image = image
        news.content = content
        SESSION.commit()


    def delete(self, id):
        SESSION.query(News).get(id).delete()
        SESSION.commit()
