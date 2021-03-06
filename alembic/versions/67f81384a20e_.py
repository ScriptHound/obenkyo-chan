"""empty message

Revision ID: 67f81384a20e
Revises: 0afdfc0635fe
Create Date: 2021-02-25 22:22:34.872241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67f81384a20e'
down_revision = '0afdfc0635fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hiragana_cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('transcription', sa.UnicodeText(), nullable=True),
    sa.Column('cyrillic', sa.UnicodeText(), nullable=True),
    sa.Column('original_appearance', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('original_appearance')
    )
    op.create_table('katakana_cards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('transcription', sa.UnicodeText(), nullable=True),
    sa.Column('cyrillic', sa.UnicodeText(), nullable=True),
    sa.Column('original_appearance', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('original_appearance')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('katakana_cards')
    op.drop_table('hiragana_cards')
    # ### end Alembic commands ###
