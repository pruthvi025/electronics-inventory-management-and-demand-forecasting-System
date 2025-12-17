import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


_BASE_DIR = Path(__file__).resolve().parents[3]

# Load environment variables from optional .env locations (project root and secrets folder)
load_dotenv(_BASE_DIR / ".env")
load_dotenv(_BASE_DIR / "secrets" / ".env")

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
	raise RuntimeError("DATABASE_URL environment variable is required")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()
