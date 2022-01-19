from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Permission(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    key = Column(String, unique=True, index=True, nullable=False)
    name = Column(String)
