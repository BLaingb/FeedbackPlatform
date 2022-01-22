

from app.modules.auth.models.role import Role
from app.repositories.base import BaseRepository


class RoleRepository(BaseRepository[Role, Role, Role]):
    pass


role = RoleRepository(Role)
