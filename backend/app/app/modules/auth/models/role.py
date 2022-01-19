from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class RolePermissions(Base):
    permission_id = Column(Integer, ForeignKey('permission.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)


class UserRoles(Base):
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)


class Role(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    permissions = relationship(
        "Permission",
        secondary=RolePermissions,
        backref="roles"
    )
    users = relationship(
        "User",
        secondary=UserRoles,
        backref="roles"
    )
