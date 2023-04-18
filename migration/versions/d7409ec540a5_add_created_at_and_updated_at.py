"""add created_at and updated_at

Revision ID: d7409ec540a5
Revises: 36ff736d8bb5
Create Date: 2023-04-18 09:45:08.989121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7409ec540a5'
down_revision = '36ff736d8bb5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('city', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('city', sa.Column('updated_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('city', 'updated_at')
    op.drop_column('city', 'created_at')
    # ### end Alembic commands ###