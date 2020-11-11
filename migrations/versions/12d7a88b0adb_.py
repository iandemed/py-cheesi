"""empty message

Revision ID: 12d7a88b0adb
Revises: bbf7443ef38c
Create Date: 2020-11-10 19:48:02.717561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12d7a88b0adb'
down_revision = 'bbf7443ef38c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('aroma_cheese_id_fkey', 'aroma', type_='foreignkey')
    op.create_foreign_key(None, 'aroma', 'cheese', ['cheese_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('country_cheese_id_fkey', 'country', type_='foreignkey')
    op.create_foreign_key(None, 'country', 'cheese', ['cheese_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('milk_cheese_id_fkey', 'milk', type_='foreignkey')
    op.create_foreign_key(None, 'milk', 'cheese', ['cheese_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('texture_cheese_id_fkey', 'texture', type_='foreignkey')
    op.create_foreign_key(None, 'texture', 'cheese', ['cheese_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    op.drop_constraint('type_cheese_id_fkey', 'type', type_='foreignkey')
    op.create_foreign_key(None, 'type', 'cheese', ['cheese_id'], ['id'], onupdate='CASCADE', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'type', type_='foreignkey')
    op.create_foreign_key('type_cheese_id_fkey', 'type', 'cheese', ['cheese_id'], ['id'])
    op.drop_constraint(None, 'texture', type_='foreignkey')
    op.create_foreign_key('texture_cheese_id_fkey', 'texture', 'cheese', ['cheese_id'], ['id'])
    op.drop_constraint(None, 'milk', type_='foreignkey')
    op.create_foreign_key('milk_cheese_id_fkey', 'milk', 'cheese', ['cheese_id'], ['id'])
    op.drop_constraint(None, 'country', type_='foreignkey')
    op.create_foreign_key('country_cheese_id_fkey', 'country', 'cheese', ['cheese_id'], ['id'])
    op.drop_constraint(None, 'aroma', type_='foreignkey')
    op.create_foreign_key('aroma_cheese_id_fkey', 'aroma', 'cheese', ['cheese_id'], ['id'])
    # ### end Alembic commands ###
