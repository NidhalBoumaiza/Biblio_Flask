"""Add role column to adherents table

Revision ID: cccdbb475abc
Revises: ac5fffaa8a01
Create Date: 2025-01-10 00:31:55.592415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cccdbb475abc'
down_revision = 'ac5fffaa8a01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('adherents', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('adherents', schema=None) as batch_op:
        batch_op.drop_column('role')

    # ### end Alembic commands ###
