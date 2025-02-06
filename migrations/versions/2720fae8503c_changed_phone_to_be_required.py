"""changed phone to be required

Revision ID: 2720fae8503c
Revises: deef66e20565
Create Date: 2025-02-06 08:42:07.076274

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2720fae8503c'
down_revision: Union[str, None] = 'deef66e20565'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'phone',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'phone',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    # ### end Alembic commands ###
