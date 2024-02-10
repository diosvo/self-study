# Third-party Packages
from fastapi import FastAPI

# Development Modules
from . import models
from .database import engine
from .routers import auth, posts, users

models.Base.metadata.create_all(bind=engine)

"""APP & SWAGGER CONFIGURATION"""

TAGS_METADATA = [
    {
        "name": auth.TAG_NAME,
        "description": "The **login** logic is also here."
    },
    {
        "name": posts.TAG_NAME,
        "description": "Manage posts."
    },
    {
        "name": users.TAG_NAME,
        "description": "Operations with users.",
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

APP_ROUTERS = [
    auth.router,
    posts.router,
    users.router,
]
for router in APP_ROUTERS:
    app.include_router(router)
