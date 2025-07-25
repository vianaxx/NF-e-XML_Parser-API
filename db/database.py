from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./nfe.db"  # pode trocar para PostgreSQL depois

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # só para SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
