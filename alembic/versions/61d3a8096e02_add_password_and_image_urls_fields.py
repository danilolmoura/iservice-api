"""Add password and image_urls fields

Revision ID: 61d3a8096e02
Revises: 53f6875aa5d2
Create Date: 2020-09-04 21:34:37.605998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61d3a8096e02'
down_revision = '53f6875aa5d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('image_urls', sa.ARRAY(sa.String(length=128)), nullable=True))
    op.add_column('user', sa.Column('password', sa.String(length=24), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    op.drop_column('product', 'image_urls')
    # ### end Alembic commands ###
