# Python Libraries
import logging

# Third-party Packages
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

# Development Modules
from .. import models, oauth2, schemas
from ..database import get_database

TAG_NAME = "vote"
logger = logging.getLogger("uvicorn")

router = APIRouter(
    prefix=f"/{TAG_NAME}",
    tags=[TAG_NAME],
    dependencies=[Depends(oauth2.get_current_user)]
)


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED
)
def vote(
    vote: schemas.Vote,
    request: Request,
    db: Session = Depends(get_database),
) -> None:
    # Constant values
    post_id = vote.post_id
    user_id = request.state.current_user.id

    # Check whether the post exists or not
    post = db.query(models.Post).filter(models.Post.id == post_id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {post_id} does not exist."
        )

    # Find the exact vote and either vote or unvote on it.
    query = db.query(models.Vote) \
        .filter(models.Vote.post_id == post_id, models.Vote.user_id == user_id)
    found_vote = query.first()

    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User {user_id} has already voted on post {post_id}."
            )

        new_vote = models.Vote(post_id=post_id, user_id=user_id)

        db.add(new_vote)
        db.commit()

        logger.info("⬆️ Voted")

        return
    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Vote does not exist."
            )

        query.delete(synchronize_session=False)
        db.commit()

        logger.info("⬇️ Unvoted")

        return
