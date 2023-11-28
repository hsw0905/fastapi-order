from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app.config import config

engine = create_engine(
    url=config.DB_URL, echo=config.DB_ECHO, pool_pre_ping=config.DB_PRE_PING
)

session_factory = sessionmaker(bind=engine, autoflush=False, autocommit=False)

session = scoped_session(session_factory=session_factory)
