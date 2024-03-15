from sqlalchemy import MetaData, create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# MySQLconnection
URL_DATA_BASE = "mysql+pymysql://root:1234@localhost:3306/todoapplication"
engine = create_engine(URL_DATA_BASE)
# creates a new SQLAlchemy session object each time it's called.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


