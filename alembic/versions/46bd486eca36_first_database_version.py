"""First database version

Revision ID: 46bd486eca36
Revises: 
Create Date: 2020-08-20 18:36:30.204221

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2

# revision identifiers, used by Alembic.
revision = '46bd486eca36'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('description', sa.String(length=512), nullable=False),
    sa.Column('category', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('store',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('location', geoalchemy2.types.Geometry(geometry_type='POINT', from_text='ST_GeomFromEWKT', name='geometry'), nullable=False),
    sa.Column('coverage_area', geoalchemy2.types.Geometry(geometry_type='MULTIPOLYGON', from_text='ST_GeomFromEWKT', name='geometry'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_store_coverage_area'), 'store', ['coverage_area'], unique=False)
    op.create_index(op.f('ix_store_location'), 'store', ['location'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('document', sa.String(length=128), nullable=False),
    sa.Column('store_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['store_id'], ['store.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('document'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('store_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_index(op.f('ix_store_location'), table_name='store')
    op.drop_index(op.f('ix_store_coverage_area'), table_name='store')
    op.drop_table('store')
    op.drop_table('product')
    # ### end Alembic commands ###
