"""empty message

Revision ID: 0c9f557b12d7
Revises: 75af2e77cd80
Create Date: 2021-03-09 21:36:37.908354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c9f557b12d7'
down_revision = '75af2e77cd80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('drug_exposure', sa.Column('visit_detail_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('drug_exposure', 'visit_detail_id')
    # ### end Alembic commands ###
