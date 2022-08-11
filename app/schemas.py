from pydantic import BaseModel, EmailStr
from datetime import datetime

##Handling Requests
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

##Handling Responses
class Post(PostBase):
    id: int
    published_at: datetime
    class Config:
        orm_mode = True ##convert sqlalchemy model to pydantic schema

##Handling Requests
class UserCreate(BaseModel):
    email: EmailStr
    password: str

##Handling Responses
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True ##convert sqlalchemy model to pydantic schema

class UserLogin(BaseModel):
    email: EmailStr
    password: str