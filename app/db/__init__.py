from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

from app.config import Config


Base = declarative_base()
engine = create_engine(Config.db_uri, future=True, connect_args={"check_same_thread": False})


def get_session():
    with Session(engine) as sess:
        yield sess
