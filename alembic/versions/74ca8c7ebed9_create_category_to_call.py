"""Create category_to_call

Revision ID: 74ca8c7ebed9
Revises: 9c27c657a97d
Create Date: 2024-10-02 11:09:34.122107

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74ca8c7ebed9'
down_revision: Union[str, None] = '9c27c657a97d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'category_to_call',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('category_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['category_id'], ['category.id'], ondelete='CASCADE', onupdate='CASCADE'),
        sa.Column('call_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['call_id'], ['call.id'], ondelete='CASCADE', onupdate='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    op.drop_table('category_to_call')
