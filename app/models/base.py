from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

DATABASE_INFO = {
    "user": "root",
    "password": "1234567890",
    "host": "mariadb",
    "port": "3306" 
} 

# Define the MariaDB engine using MariaDB Connector/Python
ENGINE = sqlalchemy.create_engine(
    f"mariadb+mariadbconnector://{DATABASE_INFO['user']}:{DATABASE_INFO['password']}@{DATABASE_INFO['host']}:{DATABASE_INFO['port']}/esnews"
)

BASE = declarative_base()

# Create a session
SESSION = sqlalchemy.orm.sessionmaker()
SESSION.configure(bind=ENGINE)
SESSION = SESSION()