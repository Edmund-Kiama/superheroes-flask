"""adds models

Revision ID: 44f19c1bb858
Revises: 
Create Date: 2025-03-30 09:03:03.881720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44f19c1bb858'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('heroes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('super_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_heroes'))
    )
    op.create_table('powers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_powers'))
    )
    op.create_table('hero_powers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('strength', sa.String(), nullable=True),
    sa.Column('hero_id', sa.Integer(), nullable=True),
    sa.Column('power_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hero_id'], ['heroes.id'], name=op.f('fk_hero_powers_hero_id_heroes')),
    sa.ForeignKeyConstraint(['power_id'], ['powers.id'], name=op.f('fk_hero_powers_power_id_powers')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_hero_powers'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hero_powers')
    op.drop_table('powers')
    op.drop_table('heroes')
    # ### end Alembic commands ###
