# Python Libraries
import logging
import time
from typing import Optional

# Third-party Packages
import psycopg2
from fastapi import FastAPI, HTTPException, status
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel

logger = logging.getLogger('uvicorn')

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


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
def get_posts() -> list[Post]:
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()

    return posts


@app.get("/posts/{id}")
def get_post(id: int) -> Post:
    cursor.execute(
        f"""
        SELECT * FROM posts
        WHERE id={id}
        """,
    )
    post = cursor.fetchone()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} was not found."
        )

    return post


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post) -> Post:
    cursor.execute(
        """
        INSERT INTO posts (title, content, published)
        VALUES (%s, %s, %s)
        RETURNING *
        """,
        (post.title, post.content, post.published)
    )
    new_post = cursor.fetchone()

    conn.commit()

    return new_post


@app.put("/posts/{id}")
def update_post(id: int, post: Post) -> Post:
    cursor.execute(
        """
        UPDATE posts
        SET title = %s, content = %s, published = %s
        WHERE id = %s
        RETURNING *
        """,
        (post.title, post.content, post.published, str(id))
    )
    updated_post = cursor.fetchone()

    conn.commit()

    if updated_post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} does not exist."
        )

    return updated_post


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int) -> None:
    cursor.execute(
        f"""
        DELETE FROM posts
        WHERE id={id}
        RETURNING *
        """,
    )
    deleted_post = cursor.fetchone()

    conn.commit()

    if deleted_post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} does not exist."
        )

    return
