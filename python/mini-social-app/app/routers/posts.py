# Python Libraries
import logging

# Third-party Packages
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

# Development Modules
from .. import models, oauth2, schemas
from ..database import get_database

TAG_NAME = "posts"
logger = logging.getLogger("uvicorn")

router = APIRouter(
    prefix=f"/{TAG_NAME}",
    tags=[TAG_NAME],
    dependencies=[Depends(oauth2.get_current_user)]
)


@router.get(
    path="/",
    response_model=list[schemas.PostsResponse],
)
def get_posts(
    skip: int = 0,
    limit: int = 10,
    query: str = "",
    db: Session = Depends(get_database),
):
    posts = db.query(models.Post) \
        .filter(models.Post.title.contains(query)) \
        .limit(limit) \
        .offset(skip) \
        .all()

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
def create_post(
    request: Request,
    post: schemas.Post,
    db: Session = Depends(get_database)
):
    new_post = models.Post(
        owner_id=request.state.current_user.id,
        **post.model_dump()
    )

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
    request: Request,
    updated_post: schemas.Post,
    db: Session = Depends(get_database)
):
    query = db.query(models.Post).filter(models.Post.id == id)
    post: models.Post = query.first()

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} does not exist."
        )

    if post.owner_id != request.state.current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to perform the delete action."
        )

    query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()

    return query.first()


@router.delete(
    path="/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_post(
    id: int,
    request: Request,
    db: Session = Depends(get_database)
) -> None:
    query = db.query(models.Post).filter(models.Post.id == id)
    post: models.Post = query.first()

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} does not exist."
        )

    if post.owner_id != request.state.current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Not authorized to perform the delete action."
        )

    query.delete(synchronize_session=False)
    db.commit()

    return
