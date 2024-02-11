# Python Libraries
from datetime import datetime

# Third-party Packages
from pydantic import BaseModel, EmailStr


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


class User(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int | None = None


class Response(Post):
    """
    TODO

    Modify the `Response` class so that it can be a general class used for other classes such as `Post`, `User`, etc. It will include some common parameters:

    * `id`
    * `created_at`

    But also exclude specific parameters that are sensitive (e.g., `password`), if possible.
    """

    id: int
    created_at: datetime

    class Config:
        from_attributes = True
