from sqlalchemy import Column, Integer, ForeignKey

from src.models.base import Base


class CategoryToCall(Base):
    __tablename__ = 'category_to_call'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    call_id = Column(Integer, ForeignKey('call.id'))
