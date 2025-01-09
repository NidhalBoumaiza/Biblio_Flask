"""Create tables

Revision ID: 46cb3a8e03ec
Revises: 
Create Date: 2024-12-31 06:32:33.365355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46cb3a8e03ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auteurs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=50), nullable=False),
    sa.Column('prenom', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nom')
    )
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nom')
    )
    op.create_table('adherents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('adresse', sa.String(length=200), nullable=False),
    sa.Column('date_naissance', sa.Date(), nullable=False),
    sa.Column('num_carte_identite', sa.String(length=20), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('nbr_conx', sa.Integer(), nullable=True),
    sa.Column('password_changed', sa.Boolean(), nullable=True),
    sa.Column('nbr_emprunts', sa.Integer(), nullable=True),
    sa.Column('classe_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['classe_id'], ['classes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('num_carte_identite'),
    sa.UniqueConstraint('username')
    )
    op.create_table('livres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titre', sa.String(length=100), nullable=False),
    sa.Column('nbre_pages', sa.Integer(), nullable=False),
    sa.Column('code_auteur', sa.Integer(), nullable=False),
    sa.Column('disponible', sa.Boolean(), nullable=True),
    sa.Column('nbre_exemplaires', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['code_auteur'], ['auteurs.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('titre')
    )
    op.create_table('emprunts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_debut', sa.Date(), nullable=False),
    sa.Column('date_retour', sa.Date(), nullable=True),
    sa.Column('adherent_id', sa.Integer(), nullable=False),
    sa.Column('livre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['adherent_id'], ['adherents.id'], ),
    sa.ForeignKeyConstraint(['livre_id'], ['livres.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emprunts')
    op.drop_table('livres')
    op.drop_table('adherents')
    op.drop_table('genres')
    op.drop_table('classes')
    op.drop_table('auteurs')
    # ### end Alembic commands ###
