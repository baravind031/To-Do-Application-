from pydantic import BaseModel
from typing import Optional



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

