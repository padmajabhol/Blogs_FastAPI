from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# creating the path and connecting it to the db
SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'

# creating the engine
engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

# create session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

# declare mapping
Base = declarative_base()

# db connection


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
