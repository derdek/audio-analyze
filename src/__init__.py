from src.db import engine
from src.models.base import Base

Base.metadata.create_all(bind=engine)
