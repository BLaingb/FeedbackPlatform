"""seed role permissions

Revision ID: a4bb74029704
Revises: 58a7802cbd68
Create Date: 2022-01-22 15:16:14.375158

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = 'a4bb74029704'
down_revision = '58a7802cbd68'
branch_labels = None
depends_on = None


def upgrade():
    permissions_table = table(
        "permission",
        column("id", sa.Integer),
        column("key", sa.String),
        column("name", sa.String),
    )
    op.bulk_insert(
        permissions_table,
        [
            {"key": "role.create", "name": "Create a new role"},
            {"key": "role.list", "name": "Get the list of roles"},
            {"key": "role.edit", "name": "Edit  role's information"},
            {"key": "role.delete", "name": "Delete a role"},
        ]
    )


def downgrade():
    op.execute(
        "DELETE FROM permission WHERE key IN "
        "('role.create', 'role.list', 'role.edit', 'role.delete');"
    )
