# Third-party Packages
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])

"""Authentication & Authorization

The purpose is to help hash and verify the user password
"""


def hash(password: str) -> str:
    return pwd_context.hash(password)


def verify(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
