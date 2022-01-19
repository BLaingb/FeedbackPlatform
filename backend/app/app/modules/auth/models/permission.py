from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.modules.auth.models.role import Role, RolePermissions # noqa


class Permission(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    key = Column(String, unique=True, index=True, nullable=False)
    name = Column(String)

    roles = relationship(
        "Role",
        secondary="rolepermissions",
        back_populates="permissions"
    )
