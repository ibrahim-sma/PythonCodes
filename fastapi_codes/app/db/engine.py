from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/fmtc_db"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
