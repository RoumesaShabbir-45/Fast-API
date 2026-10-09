from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from fastapi import FastAPI

app = FastAPI()
database_url = "sqlite:///./users.db"
engine = create_engine(database_url, connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

