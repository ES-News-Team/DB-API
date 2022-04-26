from app import db_api

@db_api.route('/')
def index():
    return 'Hello :)'