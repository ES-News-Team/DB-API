from app.controllers.news_controller import NewsController 
from flask import request
from flask_restful import Resource
from app import api

NEWS = NewsController()

class NewsAPI(Resource):

    def post(self):
        data = request.get_json()
        NEWS.create(data['title'], data['image'], data['content'])

        return 'News created', 201


    def put(self, id):
        id = str(id)
        data = request.get_json()
        NEWS.update(id, data['title'], data['image'], data['content'])
        
        return 'News updated', 200


    def delete(self, id):
        id = str(id)
        NEWS.delete(id)
    
        return 'News Deleted', 200


    def get(self, id=None):
        if not id:
            list_of_news = NEWS.list()
            response = []

            for news in list_of_news:
                response.append({
                    "id": news.id,
                    "title": news.title,
                    "image": news.image,
                    "content": news.content 
                })
            
            response = {
                "news": response,
                "length": len(response)
            }

            return response, 200

        id = str(id)
        retrieved_news = NEWS.retrieve(id)

        response = {
            "id": retrieved_news.id,
            "title": retrieved_news.title,
            "image": retrieved_news.image,
            "content": retrieved_news.content 
        }
        
        return response, 200

api.add_resource(NewsAPI, '/news/', '/news/<uuid:id>')