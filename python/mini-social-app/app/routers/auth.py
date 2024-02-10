# Third-party Packages
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# Development Modules
from .. import database, models, schemas, utils

TAG_NAME = "auth"

router = APIRouter(
    tags=[TAG_NAME],
)


@router.post("/token")
def login_for_access_token(
    input: schemas.User,
    db: Session = Depends(database.get_database)
) -> dict[str, str]:
    query = db.query(models.User).filter(models.User.email == input.email)
    user = query.first()

    if not user or not utils.verify(input.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Incorrect email or password."
        )

    # Create and return a token

    return {
        "token": "<token>"
    }
