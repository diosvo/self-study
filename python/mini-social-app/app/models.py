# Third-party Packages
from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, String, text

# Development modules
from .database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default='TRUE')
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text('now()')
    )
