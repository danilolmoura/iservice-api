"""add products status field

Revision ID: 767392988264
Revises: 61d3a8096e02
Create Date: 2020-09-05 22:19:16.646783

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '767392988264'
down_revision = '61d3a8096e02'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.add_column('product', sa.Column('is_exchange', sa.Boolean(), nullable=False))
    op.add_column('product', sa.Column('is_for_sale', sa.Boolean(), nullable=False))
    op.alter_column('product', 'image_urls',
               existing_type=postgresql.ARRAY(sa.VARCHAR(length=512)),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'image_urls',
               existing_type=postgresql.ARRAY(sa.VARCHAR(length=128)),
               nullable=True)
    op.drop_column('product', 'is_for_sale')
    op.drop_column('product', 'is_exchange')
    op.drop_column('product', 'is_active')
    # ### end Alembic commands ###
