# Python Libraries
from datetime import datetime, timedelta, timezone

# Third-party Packages
from jose import jwt

"""
To get a secret key, run:

```bash
openssl rand -hex 32
```
"""
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = "60f69997cadadbde3a91fb10d584d310d2a1e0e6380d696dde63ca2d5a641fbd"


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + \
        timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        claims=to_encode,
        key=SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt
