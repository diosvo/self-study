# Third-party Packages
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

# Development Modules
from .. import database, models, oauth2, schemas, utils

TAG_NAME = "auth"

router = APIRouter(
    tags=[TAG_NAME],
)


@router.post("/token")
def login_for_access_token(
    input: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_database)
) -> schemas.Token:
    query = db.query(models.User).filter(models.User.email == input.username)
    user = query.first()

    if not user or not utils.verify(input.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Incorrect username or password."
        )

    access_token = oauth2.create_access_token({
        "user_id": user.id
    })

    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }
