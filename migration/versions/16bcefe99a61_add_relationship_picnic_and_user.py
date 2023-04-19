"""add relationship picnic and user

Revision ID: 16bcefe99a61
Revises: 9e948ab3f490
Create Date: 2023-04-19 21:11:00.675425

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "16bcefe99a61"
down_revision = "9e948ab3f490"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "picnic_user",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("picnic_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["picnic_id"],
            ["picnic.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id", "picnic_id", "user_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("picnic_user")
    # ### end Alembic commands ###