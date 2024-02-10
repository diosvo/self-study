# Third-party Packages
from fastapi import FastAPI

# Development Modules
from . import models
from .database import engine
from .routers import posts, users

models.Base.metadata.create_all(bind=engine)

"""APP & SWAGGER CONFIGURATION"""

TAGS_METADATA = [
    {
        "name": posts.TAG_NAME,
        "description": "Manage posts."
    },
    {
        "name": users.TAG_NAME,
        "description": "Operations with users. The **login** logic is also here.",
    },
]

app = FastAPI(
    title="Mini Social App",
    version="1.0.0",
    contact={
        "name": "Dios Vo",
        "email": "vtmn1212@gmail.com"
    },
    openapi_tags=TAGS_METADATA,
)

app.include_router(posts.router)
app.include_router(users.router)
