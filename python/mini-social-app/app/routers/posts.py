# Python Libraries
import logging

# Third-party Packages
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Development Modules
from .. import models, schemas
from ..database import get_database

TAG_NAME = "posts"
logger = logging.getLogger("uvicorn")

router = APIRouter(
    prefix=f"/{TAG_NAME}",
    tags=[TAG_NAME],
)


@router.get(
    path="/",
    response_model=list[schemas.Response],
)
def get_posts(db: Session = Depends(get_database)):
    posts = db.query(models.Post).all()

    return posts


@router.get(
    path="/{id}",
    response_model=schemas.Response,
)
def get_post(id: int, db: Session = Depends(get_database)):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} was not found."
        )

    return post


@router.post(
    path="/",
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


@router.put(
    path="/{id}",
    response_model=schemas.Response,
)
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


@router.delete(
    path="/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
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
