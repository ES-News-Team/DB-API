from app import db_api


if __name__ == "__main__":
  
  db_api.run(host="0.0.0.0", port=5002, debug=True)