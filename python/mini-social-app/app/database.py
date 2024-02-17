from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "diosvo:1234@localhost/fastapi"
SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_URL}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_database():
    """
    Ensure the database session is always closed after the request.
    Even if there was an exception while processing the request.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
