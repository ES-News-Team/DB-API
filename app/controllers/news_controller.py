from app.models.base import SESSION
from app.models.news import News
from sqlalchemy import select
from app.controllers.controller_interface import IController
from app.models.base import SESSION
class NewsController(IController):
       
    def list(self):
        try:
            result = SESSION.query(News).all()
            return result
        except:
            SESSION.rollback()

    
    def retrieve(self, id: str):
        stmt = select(News).where(News.id == id)
        news = SESSION.scalars(stmt).one()
        return news
      

    def create(self, title, image, content):  
        newNews = News(title=title, image=image, content=content)
        try: 
            SESSION.add(newNews)
            SESSION.commit()
        except:
            SESSION.rollback()


    def update(self, id, title, image, content):
        try:
            news = SESSION.query(News).get(id)
            news.title = title
            news.image = image
            news.content = content
            SESSION.commit()
        except:
            SESSION.rollback()

    def delete(self, id):
        try:
            news = SESSION.query(News).get(id)
            SESSION.delete(news)
            SESSION.commit()
        except:
            SESSION.rollback()
