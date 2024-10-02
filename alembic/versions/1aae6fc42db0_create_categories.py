"""Create categories

Revision ID: 1aae6fc42db0
Revises: f8ddeb0d8aaf
Create Date: 2024-10-02 10:59:45.008768

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1aae6fc42db0'
down_revision: Union[str, None] = 'f8ddeb0d8aaf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'category',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=30), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('category')
