import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import app.models
from app.database.base import Base
from app.database.connection import engine
Base.metadata.create_all(engine)
print("Tables created or already exist:", sorted(Base.metadata.tables.keys()))
