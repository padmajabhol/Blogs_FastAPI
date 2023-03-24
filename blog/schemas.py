from pydantic import BaseModel
from typing import List, Optional


class Login(BaseModel):
    username: str
    password: str

# JWT Token


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

# Blog pydantic models


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config():
        orm_mode = True

# User pydantic models


class User(BaseModel):
    name: str
    email: str
    password: str

# response_model


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

# used in response_model thus uses orm
    class Config():
        orm_mode = True

# response model


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True
