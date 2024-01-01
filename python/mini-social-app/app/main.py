from random import randrange
from typing import Optional

from fastapi import FastAPI, HTTPException, status

from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


list_posts = [
    {
        "id": 1,
        "title": "Random Post 1",
        "content": "Content of post 1",
    },
    {
        "id": 2,
        "title": "Favorite foods",
        "content": "I like pizza!",
    }
]


def find_posts(id: int) -> Post:
    for post in list_posts:
        if post["id"] == id:
            return post


def find_index_post(id: int) -> int:
    for index, post in enumerate(list_posts):
        if post["id"] == id:
            return index


@app.get("/posts")
def get_posts():
    return list_posts


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randrange(0, 10000000)
    list_posts.append(post_dict)
    return post_dict


@app.get("/posts/{id}")
def get_post(id: int):
    post = find_posts(id)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} was not found."
        )

    return post


@app.patch("/posts/{id}")
def update_posts(id: int, post: Post):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} does not exist."
        )
    
    post_dict = post.model_dump()
    post_dict['id'] = id
    list_posts[index] = post_dict

    return post_dict


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id: int):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {id} does not exist."
        )

    list_posts.pop(index)

    return
