# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa

# Auth
from app.modules.auth.models.role import Role, RolePermissions, UserRoles  # noqa
from app.modules.auth.models.user import User  # noqa
from app.modules.auth.models.permission import Permission  # noqa

# Chapters
from app.modules.chapters.models.chapter import Chapter # noqa