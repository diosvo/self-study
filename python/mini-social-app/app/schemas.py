from datetime import datetime

from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str
    published: bool = True

class Response(Post):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True