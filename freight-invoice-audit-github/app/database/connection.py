import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

ROOT_DIR = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_DIR / ".env")

host = os.getenv("DB_HOST", "127.0.0.1")
port = os.getenv("DB_PORT", "3306")
user = os.getenv("DB_USER", "root")
password = os.getenv("DB_PASSWORD", "")
database = os.getenv("DB_NAME", "freight_audit")

engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}",
    pool_pre_ping=True
)

def test_connection():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("Connected successfully!")
        print("Database:", database)
