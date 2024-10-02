from typing import Optional
from sqlalchemy import Column, Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from src.models.base import Base


class Call(Base):
    __tablename__ = "call"
    id: int = Column(Integer, primary_key=True)
    name: Optional[str] = Column(String(30))
    location: Optional[str] = Column(String(30))
    emotional_tone: Optional[str] = Column(String(30))
    text: Optional[str] = Column(String(30))

    # categories = relationship("Category", secondary="category_to_call")
