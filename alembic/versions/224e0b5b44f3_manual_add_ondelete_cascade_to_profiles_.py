"""manual: add ondelete cascade to profiles.user_id

Revision ID: 224e0b5b44f3
Revises: 86c17cd99367
Create Date: 2025-10-16 14:26:12.677909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '224e0b5b44f3'
down_revision: Union[str, Sequence[str], None] = '86c17cd99367'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
