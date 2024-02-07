# Python Libraries
import logging

# Third-party Packages
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas
from .database import engine, get_database

logger = logging.getLogger('uvicorn')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get(path="/posts", response_model=list[schemas.Response])
def get_posts(db: Session = Depends(get_database)):
    posts = db.query(models.Post).all()

    return posts


@app.get(path="/posts/{id}", response_model=schemas.Response)
def get_post(id: int, db: Session = Depends(get_database)):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} was not found."
        )

    return post


@app.post(
    path="/posts",
    response_model=schemas.Response,
    status_code=status.HTTP_201_CREATED,
)
def create_post(post: schemas.Post, db: Session = Depends(get_database)):
    new_post = models.Post(**post.model_dump())

    # Add the instance object to database session
    db.add(new_post)
    # The data is saved
    db.commit()
    # Contain new data from the database, liked the generated ID
    db.refresh(new_post)

    return new_post


@app.put(path="/posts/{id}", response_model=schemas.Response)
def update_post(
    id: int,
    updated_post: schemas.Post,
    db: Session = Depends(get_database)
):
    query_post = db.query(models.Post).filter(models.Post.id == id)

    if query_post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} does not exist."
        )

    query_post.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()

    return query_post.first()


@app.delete(path="/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_database)) -> None:
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} does not exist."
        )

    post.delete(synchronize_session=False)
    db.commit()

    return


"""USERS

Authentication & Authorization with JWT
"""


@app.post(
    path="/users",
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: schemas.User, db: Session = Depends(get_database)):
    try:
        new_user = models.User(**user.model_dump())
        db.add(new_user)
        db.commit()

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc).split('\n')[1]
        )

    else:
        db.refresh(new_user)

        return new_user
