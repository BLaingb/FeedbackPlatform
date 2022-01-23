
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modules.auth.models.user import User # noqa


class Chapter(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False, index=True)

    # Relationships to 'auth' module
    chapter_lead_id = Column(Integer, ForeignKey('user.id'))
    chapter_lead = relationship("User", foreign_keys="Chapter.chapter_lead_id")
    members = relationship(
        "User",
        back_populates="chapter",
        foreign_keys="User.chapter_id"
    )
