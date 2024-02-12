# Python Libraries
from datetime import datetime, timedelta

# Third-party Packages
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

# Development Modules
from . import database, models, schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


"""
To get a secret key, run:

```bash
openssl rand -hex 32
```
"""
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOUR = 1
SECRET_KEY = "60f69997cadadbde3a91fb10d584d310d2a1e0e6380d696dde63ca2d5a641fbd"


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOUR)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        claims=to_encode,
        key=SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


def verify_access_token(
    token: str,
    credentials_exception: HTTPException
) -> int:
    try:
        payload = jwt.decode(
            token=token,
            key=SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        id: int = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id=id)

    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(
    request: Request,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(database.get_database),
) -> models.User | None:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()

    if user is None:
        raise credentials_exception

    # Store additional information on the request
    request.state.current_user = user

    return user
