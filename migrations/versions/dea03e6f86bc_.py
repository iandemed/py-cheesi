"""empty message

Revision ID: dea03e6f86bc
Revises: a56287ed831a
Create Date: 2021-05-07 21:01:32.474852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dea03e6f86bc'
down_revision = 'a56287ed831a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('milk', 'pasteurized')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('milk', sa.Column('pasteurized', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
