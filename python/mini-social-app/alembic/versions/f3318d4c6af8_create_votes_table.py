"""Create `votes` tables

Revision ID: f3318d4c6af8
Revises: 8bc915eeea49
Create Date: 2024-02-18 00:08:00.416478

"""
# Third-party Packages
from alembic import op
from sqlalchemy import Column, ForeignKey, Integer

# Revision identifiers, used by Alembic.
revision: str = "f3318d4c6af8"
down_revision: str = "8bc915eeea49"

CASCADE = "CASCADE"
TABLE_NAME = "votes"


def upgrade() -> None:
    op.create_table(
        TABLE_NAME,
        Column(
            "user_id",
            Integer,
            ForeignKey("users.id", ondelete=CASCADE),
            primary_key=True
        ),
        Column(
            "post_id",
            Integer,
            ForeignKey("posts.id", ondelete=CASCADE),
            primary_key=True
        )
    )
    pass


def downgrade() -> None:
    op.drop_table(TABLE_NAME)
    pass
