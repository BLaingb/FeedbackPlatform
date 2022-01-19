from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .role import User  # noqa
    from .permission import Permission  # noqa


class RolePermissions(Base):
    permission_id = Column(Integer, ForeignKey('permission.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)


class UserRoles(Base):
    user_id = Column(
        Integer,
        ForeignKey('user.id'),
        primary_key=True
    )
    role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)


class Role(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    permissions = relationship(
        "Permission",
        secondary="rolepermissions",
        back_populates="roles"
    )
    users = relationship(
        "User",
        secondary="userroles",
        back_populates="roles"
    )
