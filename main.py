from fastapi import FastAPI, Depends, status, HTTPException
import models.models as models
from db.database import engine, SessionLocal
from sqlalchemy.orm import Session 
import uvicorn
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from models.models import User_DB
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import Optional
import jwt
import os
os.environ["SECRET_KEY"] = "NvMio0AfLNVzzYr2jJyXOs7A3YzCzvDKWlJNf6MmMTo"
 
app = FastAPI()
models.Base.metadata.create_all(bind=engine) 

# Schema for Todo Create

class TodoCreate(BaseModel):
    task: str
    content: str

# Schema for Todo Update
class TodoUpdateData(BaseModel):
    task: Optional[str] = None
    content: Optional[str] = None

# Schema for user registration
class UserCreate(BaseModel):
    username: str
    password: str
    email: Optional[str] = None

class UserSchema(BaseModel):
    username: str
    email: Optional[str] = None
     
# session object for database operation
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# setup authentication scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
# hashing object for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 
# route for user registration
@app.post("/register/", response_model=UserSchema)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    db_user = User_DB(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
# route for user login
@app.post("/login/")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User_DB).filter(User_DB.username == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # generate JWT token:
    access_token = jwt.encode({"sub": user.username}, "SECRET_KEY")
    return {"access_token": access_token, "token_type": "bearer"}
# route for retrieving user profile
@app.get("/profile/{id}", response_model=UserSchema)
def profile(id: int, session: Session = Depends(get_db)):
    user = session.query(User_DB).filter(User_DB.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found")
    return user
# function to create an access token
def create_access_token(data, secret_key, expires_delta):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm="HS256")
    return encoded_jwt
#crud operations start
# function to create task
@app.post("/todos/", status_code=status.HTTP_201_CREATED)
async def create_todo(Todo:TodoCreate, db: Session = Depends(get_db)):
    db_todo = models.Todo(**Todo.dict())
    db.add(db_todo)
    # Commit the changes to the database and refresh the object
    db.commit()
    return db_todo
# function to read task
@app.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(todo_id: int, db: Session = Depends(get_db)):
    retrive = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if retrive is None:
        return HTTPException(status_code=404, detail="Post Not Found")
    return retrive
# function to update task
@app.put("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def update_todo(todo_id: int,todo_update_data: TodoUpdateData, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    # Update the fields with the provided data
    for field, value in todo_update_data.dict(exclude_unset=True).items():
        setattr(db_todo, field, value)
        # Commit the changes to the database and refresh the object
        db.commit()
        db.refresh(db_todo)
    return db_todo
# function to delete task
@app.delete("/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted successfully", "deleted_todo" : db_todo}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
