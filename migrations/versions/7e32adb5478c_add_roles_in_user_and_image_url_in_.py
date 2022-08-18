"""Add roles in user and image url in products

Revision ID: 7e32adb5478c
Revises: 46e2ca13ce99
Create Date: 2022-08-17 19:25:39.036620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e32adb5478c'
down_revision = '46e2ca13ce99'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('image_url', sa.String(length=200), nullable=True))
    op.add_column('user', sa.Column('rol', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'rol')
    op.drop_column('product', 'image_url')
    # ### end Alembic commands ###
