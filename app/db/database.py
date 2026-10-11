from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from pathlib import Path
from sqlalchemy.orm import sessionmaker, declarative_base
import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/todo.db")


url = make_url(DATABASE_URL)
is_sqlite = url.get_backend_name() == "sqlite"
if is_sqlite and url.database and url.database != ":memory:":
    Path(url.database).parent.mkdir(parents=True, exist_ok=True)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if is_sqlite else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()