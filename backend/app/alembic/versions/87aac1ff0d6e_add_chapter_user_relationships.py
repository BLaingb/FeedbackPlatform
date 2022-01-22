"""Add chapter-user relationships

Revision ID: 87aac1ff0d6e
Revises: 1b7d784bdca7
Create Date: 2022-01-22 17:12:26.894269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87aac1ff0d6e'
down_revision = '1b7d784bdca7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chapter', sa.Column('chapter_lead_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'chapter', 'user', ['chapter_lead_id'], ['id'])
    op.add_column('user', sa.Column('chapter_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'chapter', ['chapter_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'chapter_id')
    op.drop_constraint(None, 'chapter', type_='foreignkey')
    op.drop_column('chapter', 'chapter_lead_id')
    # ### end Alembic commands ###
