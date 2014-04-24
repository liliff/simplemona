"""Adds blockhash linking to BonusPayouts

Revision ID: 52536bfc833b
Revises: 160f63e90b91
Create Date: 2014-04-12 13:18:24.408548

"""

# revision identifiers, used by Alembic.
revision = '52536bfc833b'
down_revision = '160f63e90b91'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bonus_payout', sa.Column('blockhash', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bonus_payout', 'blockhash')
    ### end Alembic commands ###