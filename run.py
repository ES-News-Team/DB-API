from app import db_api


if __name__ == "__main__":
  
  db_api.run(host="localhost", port=5002, debug=True)