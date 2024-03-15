from sqlalchemy import Boolean, Column, Integer, String, Index
from db.database import Base
 
 
#  creating a table to store the data in mysql
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String(99), unique=True, nullable=False)
    content = Column(String(255))

class User_DB(Base):
    __tablename__ = "user_sorage"

    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    email = Column(String(50))
    hashed_password = Column(String(255))

     
# class Todo(Base):
#     __tablename__ = "todos"

#     id = Column(Integer, primary_key=True, index=True)
#     taskName = Column(String(100), nullable=False)
#     Deadline = Column(String(255))
#     content = Column(String(255), index=True)
#     status = Column(String(255))
#     Reminder = Column(String(255))
#     completed_box = Column(Boolean, default=False)
