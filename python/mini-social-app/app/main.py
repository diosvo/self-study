# Python Libraries
import logging
import time
from typing import Optional

# Third-party Packages
import psycopg2
from fastapi import Depends, FastAPI, HTTPException, status
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import models, schemas
from .database import engine, get_database

logger = logging.getLogger('uvicorn')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


while True:
    retries = 0
    max_retries = 3

    try:
        conn = psycopg2.connect(
            host='localhost',
            database='fastapi',
            user='diosvo',
            password='1234',
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        logger.info("event=connected-to-postgres-successfully")
        break

    except Exception as exc:
        log_event = "event=could-not-connect-to-postgres-server "

        if retries < max_retries:
            retries += 1
            wait_time = retries * 2  # Exponential backoff
            logger.warning(
                log_event +
                f"retry_count={retries} "
                f"message='connection retry in {wait_time}s..' "
            )
            time.sleep(wait_time)
        else:
            logger.error(
                log_event +
                "reason='Failed to connect after several attempts.' "
                f"details='{str(exc)}'"
            )


@app.get("/posts")
def get_posts(db: Session = Depends(get_database)) -> list[Post]:
    posts = db.query(models.Post).all()

    return posts


@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_database)):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} was not found."
        )

    return post


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(
    post: Post,
    db: Session = Depends(get_database)
) -> Post:
    new_post = models.Post(**post.model_dump())

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@app.put("/posts/{id}")
def update_post(
    id: int,
    updated_post: Post,
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


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
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
