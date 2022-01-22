"""Seed chapter permissions

Revision ID: c979b4532b8b
Revises: 87aac1ff0d6e
Create Date: 2022-01-22 17:13:26.225894

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = 'c979b4532b8b'
down_revision = '87aac1ff0d6e'
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
            {"key": "chapter.create", "name": "Create a new chapter"},
            {"key": "chapter.list", "name": "Get the list of chapters"},
            {"key": "chapter.view", "name": "View a chapter and its members"},
            {"key": "chapter.edit", "name": "Edit a chapter's information"},
            {"key": "chapter.delete", "name": "Delete a chapter"},
        ]
    )


def downgrade():
    op.execute(
        "DELETE FROM permission WHERE key IN "
        "('chapter.create', 'chapter.list', 'chapter.view', "
        "'chapter.edit', 'chapter.delete');"
    )
