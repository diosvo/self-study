# Python Libraries
import logging

# Third-party Packages
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Development Modules
from .. import models, oauth2, schemas, utils
from ..database import get_database

TAG_NAME = "users"
logger = logging.getLogger("uvicorn")

router = APIRouter(
    prefix=f"/{TAG_NAME}",
    tags=[TAG_NAME],
    dependencies=[Depends(oauth2.get_current_user)]
)


@router.get(
    path="/{id}",
)
def get_user(id: int, db: Session = Depends(get_database)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {id} was not found."
        )

    return user


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: schemas.User, db: Session = Depends(get_database)):
    try:
        hashed_password = utils.hash(user.password)
        user.password = hashed_password

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
