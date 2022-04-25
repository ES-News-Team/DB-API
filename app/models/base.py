from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

# Define the MariaDB engine using MariaDB Connector/Python
ENGINE = sqlalchemy.create_engine("mariadb+mariadbconnector://root:1234567890@mariadb:3306/esnews")

BASE = declarative_base()

# Create a session
SESSION = sqlalchemy.orm.sessionmaker()
SESSION.configure(bind=ENGINE)
SESSION = SESSION()