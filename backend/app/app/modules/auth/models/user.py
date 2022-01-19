from typing import List
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
# from app.modules.auth.models.role import Role, UserRoles

from .role import Role, UserRoles  # noqa
from .permission import Permission  # noqa


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    roles = relationship("Role", secondary="userroles", back_populates="users")

    def get_permissions(self) -> List[str]:
        roles_perms = [r.permissions for r in self.roles]
        return [item.key for sublist in roles_perms for item in sublist]
