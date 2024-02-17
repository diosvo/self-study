"""Add foreign-key (FK) to `posts` table

Revision ID: 8bc915eeea49
Revises: 0f9bf7da8c7c
Create Date: 2024-02-17 23:47:33.067774

"""
# Third-party Packages
from alembic import op
from sqlalchemy import Column, ForeignKey, Integer

# Revision identifiers, used by Alembic.
revision: str = "8bc915eeea49"
down_revision: str = "0f9bf7da8c7c"

# Static values
TABLE_POSTS = "posts"
COLUMN_NAME = "owner_id"


def upgrade() -> None:
    op.add_column(
        TABLE_POSTS,
        Column(
            COLUMN_NAME,
            Integer,
            ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False
        )
    )
    pass


def downgrade() -> None:
    op.drop_column(table_name=TABLE_POSTS, column_name=COLUMN_NAME)
    pass
