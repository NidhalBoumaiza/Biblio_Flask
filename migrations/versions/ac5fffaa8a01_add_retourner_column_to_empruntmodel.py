"""Add retourner column to EmpruntModel

Revision ID: ac5fffaa8a01
Revises: 46cb3a8e03ec
Create Date: 2025-01-02 02:24:26.501091

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ac5fffaa8a01'
down_revision = '46cb3a8e03ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('adherents', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=mysql.CHAR(length=1),
               type_=sa.String(length=1),
               existing_nullable=False,
               existing_server_default=sa.text("'G'"))

    with op.batch_alter_table('emprunts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('retourner', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('emprunts', schema=None) as batch_op:
        batch_op.drop_column('retourner')

    with op.batch_alter_table('adherents', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=sa.String(length=1),
               type_=mysql.CHAR(length=1),
               existing_nullable=False,
               existing_server_default=sa.text("'G'"))

    # ### end Alembic commands ###
