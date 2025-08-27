from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # file SQLite di root project biar ntar bisa check langsung isinya lewat command Prom

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency untuk ambil session di endpoint 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
