from app.models.Base import SESSION
from app.models.news import News
from sqlalchemy import select
from app.controllers.controller_interface import IController

class NewsController(IController):
       
    def list(self):
       return select(News).all()

    
    def retrieve(self, id: str):
        stmt = select(News).where(News.uuid == id)
        news = SESSION.scalars(stmt).one()
        return news
      

    def create(self, title, image, content):  
        newNews = News(title=title, image=image, content=content)
        SESSION.add(newNews)
        SESSION.commit()


    def update(id, title, image, content):
        news = SESSION.query(News).get(id)
        news.title = title
        news.image = image
        news.content = content
        SESSION.commit()


    def delete(id):
        SESSION.query(News).get(id).delete()
        SESSION.commit()
