# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.modules.auth.models.user import User  # noqa
from app.modules.auth.models.permission import Permission  # noqa
from app.modules.auth.models.role import Role, RolePermissions, UserRoles  # noqa
