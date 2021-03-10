"""empty message

Revision ID: 75af2e77cd80
Revises: bfcae76ea3fb
Create Date: 2021-03-09 16:05:02.225409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75af2e77cd80'
down_revision = 'bfcae76ea3fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('concept', 'concept_code',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('concept', 'concept_code',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    # ### end Alembic commands ###
