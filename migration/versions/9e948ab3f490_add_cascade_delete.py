"""add cascade delete

Revision ID: 9e948ab3f490
Revises: 0541d7feea26
Create Date: 2023-04-18 13:47:52.364723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e948ab3f490'
down_revision = '0541d7feea26'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('picnic_city_id_fkey', 'picnic', type_='foreignkey')
    op.create_foreign_key(None, 'picnic', 'city', ['city_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'picnic', type_='foreignkey')
    op.create_foreign_key('picnic_city_id_fkey', 'picnic', 'city', ['city_id'], ['id'])
    # ### end Alembic commands ###
