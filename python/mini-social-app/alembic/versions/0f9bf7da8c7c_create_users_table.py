"""Create `users` table

Revision ID: 0f9bf7da8c7c
Revises: fd73b17307f6
Create Date: 2024-02-17 22:27:40.302048

"""
# Third-party Packages
from alembic import op
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

# Revision identifiers, used by Alembic.
revision: str = "0f9bf7da8c7c"
down_revision: str = "fd73b17307f6"

TABLE_NAME = "users"


def upgrade() -> None:
    op.create_table(
        TABLE_NAME,
        Column("id", Integer, nullable=False, primary_key=True),
        Column("email", String, nullable=False, unique=True),
        Column("password", String, nullable=False),
        Column(
            "created_at",
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text('now()')
        ),
        comment="Manage Users."
    )


def downgrade() -> None:
    op.drop_table(TABLE_NAME)
    pass
