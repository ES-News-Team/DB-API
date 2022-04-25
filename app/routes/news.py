from app.controllers.news_controller import NewsController 
from app import db_api
from flask import request

NEWS = NewsController()

@db_api.route('/news/', methods=['POST'])
def create_news():
    data = request.get_json()
    NEWS.create(data['title'], data['image'], data['content'])

    return 'News created', 201


@db_api.route('/news/', methods=['PUT'])
def update_news():
    data = request.get_json()
    NEWS.update(data['id'], data['title'], data['image'], data['content'])
    
    return 'News updated', 200


@db_api.route('/news/', methods=['DELETE'])
def delete_news():
    data = request.get_json()
    NEWS.delete(data['id'])
  
    return 'News Deleted', 200


@db_api.route('/news/', methods=['GET'])
def retrieve_news():
    id = request.args.get('id', type = str)
    retrieved_news = NEWS.retrieve(id)

    response = {
        "id": retrieved_news.id,
        "title": retrieved_news.title,
        "image": retrieved_news.image,
        "content": retrieved_news.content 
    }
    
    return response, 200


@db_api.route('/news/')
def list_news():
    list_of_news = NEWS.list()
    response = []

    for news in list_of_news:
        response.append({
            "id": news.id,
            "title": news.title,
            "image": news.image,
            "content": news.content 
        })
    
    return response, 200
