""" Track bonus totals paid out for a block. Renames fee column

Revision ID: 27a4875d33de
Revises: f84430b16b
Create Date: 2014-03-21 18:09:28.584639

"""

# revision identifiers, used by Alembic.
revision = '27a4875d33de'
down_revision = 'f84430b16b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('block', sa.Column('bonus_payed', sa.BigInteger(), nullable=True, server_default="0"))
    op.alter_column(u'block', u'fees', new_column_name='donated')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('block', sa.Column('fees', sa.BIGINT(), nullable=True))
    op.drop_column('block', 'donated')
    op.drop_column('block', 'bonus_payed')
    ### end Alembic commands ###
