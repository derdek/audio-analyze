"""Create calls

Revision ID: f8ddeb0d8aaf
Revises: 
Create Date: 2024-10-02 10:56:31.002673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8ddeb0d8aaf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'call',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=30), nullable=True),
        sa.Column('location', sa.String(), nullable=True),
        sa.Column('emotional_tone', sa.String(), nullable=True),
        sa.Column('text', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('call')
