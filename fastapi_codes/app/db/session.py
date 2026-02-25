from sqlalchemy.orm import sessionmaker, Session
from app.db.engine import engine
from typing import Generator

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

def get_db() -> Generator[Session, None, None]:
    """
    Provides a SQLAlchemy Session per request.
    Safe for concurrent FastAPI usage.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
