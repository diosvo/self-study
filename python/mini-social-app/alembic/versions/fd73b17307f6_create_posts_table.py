"""Create `posts` table

Revision ID: fd73b17307f6
Revises: 
Create Date: 2024-02-17 21:31:55.811527

"""
# Third-party Packages
from alembic import op
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

# Revision identifiers, used by Alembic.
revision: str = "fd73b17307f6"
down_revision = None

TABLE_NAME = "posts"


def upgrade() -> None:
    op.create_table(
        TABLE_NAME,
        Column("id", Integer, nullable=False, primary_key=True),
        Column("title", String, nullable=False),
        Column("content", String, nullable=False),
        Column("published", Boolean, nullable=False, server_default='TRUE'),
        Column(
            "created_at",
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text('now()')
        ),
    )

    pass


def downgrade() -> None:
    op.drop_table(TABLE_NAME)
    pass
