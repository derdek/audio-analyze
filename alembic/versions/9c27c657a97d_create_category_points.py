"""Create category_points

Revision ID: 9c27c657a97d
Revises: 1aae6fc42db0
Create Date: 2024-10-02 11:01:45.351874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c27c657a97d'
down_revision: Union[str, None] = '1aae6fc42db0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'category_point',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('category_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['category_id'], ['category.id'], ondelete='CASCADE', onupdate='CASCADE'),
        sa.Column('point', sa.String(length=30), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    op.drop_table('category_point')
