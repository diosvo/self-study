from datetime import datetime

from pydantic import BaseModel, EmailStr


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


class User(BaseModel):
    email: EmailStr
    password: str


class Response(Post):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
