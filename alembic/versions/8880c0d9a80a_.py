"""empty message

Revision ID: 8880c0d9a80a
Revises: 3229f2500be8
Create Date: 2021-02-28 04:41:55.467785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8880c0d9a80a'
down_revision = '3229f2500be8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meaning', sa.Column('meaning', sa.UnicodeText(), nullable=True))
    op.add_column('reading', sa.Column('reading', sa.UnicodeText(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reading', 'reading')
    op.drop_column('meaning', 'meaning')
    # ### end Alembic commands ###
