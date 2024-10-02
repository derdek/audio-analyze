from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from src.models.base import Base


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)

    points: Mapped[List["CategoryPoint"]] = relationship(back_populates="category")


class CategoryPoint(Base):
    __tablename__ = 'category_point'

    id: int = Column(Integer, primary_key=True)
    category_id: int = Column(Integer, ForeignKey('category.id'))
    point: str = Column(String(30))

    category: Mapped["Category"] = relationship(back_populates='points')
