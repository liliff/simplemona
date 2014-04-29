""" Giant rework of the Payout system.

Revision ID: 2b5117cc3df6
Revises: None
Create Date: 2014-02-25 17:44:17.487690

"""

# revision identifiers, used by Alembic.
revision = '2b5117cc3df6'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    op.drop_table('payout')
    op.drop_table('block')
    op.drop_table('transaction')
    op.drop_table('coin_transaction')
    #op.drop_table('one_minute_share')
    op.create_table('blob',
                    sa.Column('key', sa.String(), nullable=False),
                    sa.Column('data', postgresql.HSTORE(), nullable=True),
                    sa.PrimaryKeyConstraint('key')
                    )
    op.create_table('transaction',
                    sa.Column('txid', sa.String(), nullable=False),
                    sa.Column('confirmed', sa.Boolean(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('txid')
                    )
    #op.create_table('one_minute_share',
    #                sa.Column('user', sa.String(), nullable=False),
    #                sa.Column('minute', sa.DateTime(), nullable=False),
    #                sa.Column('shares', sa.Integer(), nullable=True),
    #                sa.PrimaryKeyConstraint('user', 'minute')
    #                )
    op.create_table('block',
                    sa.Column('height', sa.Integer(), nullable=False),
                    sa.Column('user', sa.String(), nullable=True),
                    sa.Column('found_at', sa.DateTime(), nullable=True),
                    sa.Column('time_started', sa.DateTime(), nullable=False),
                    sa.Column('orphan', sa.Boolean(), nullable=True),
                    sa.Column('mature', sa.Boolean(), nullable=True),
                    sa.Column('shares_to_solve', sa.BigInteger(), nullable=True),
                    sa.Column('total_value', sa.BigInteger(), nullable=True),
                    sa.Column('transaction_fees', sa.BigInteger(), nullable=True),
                    sa.Column('fees', sa.BigInteger(), nullable=True),
                    sa.Column('bits', sa.String(length=8), nullable=False),
                    sa.Column('last_share_id', sa.BigInteger(), nullable=True),
                    sa.Column('processed', sa.Boolean(), nullable=True),
                    sa.Column('hash', sa.String(), nullable=False),
                    sa.ForeignKeyConstraint(['last_share_id'], ['share.id'], ),
                    sa.PrimaryKeyConstraint('height')
                    )
    op.create_table('payout',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('blockheight', sa.Integer(), nullable=True),
                    sa.Column('user', sa.String(), nullable=True),
                    sa.Column('shares', sa.BigInteger(), nullable=True),
                    sa.Column('amount', sa.BigInteger(), nullable=True),
                    sa.Column('transaction_id', sa.String(), nullable=True),
                    sa.ForeignKeyConstraint(['blockheight'], ['block.height'], ),
                    sa.ForeignKeyConstraint(['transaction_id'], ['transaction.txid'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('user', 'blockheight')
                    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payout')
    op.drop_table('block')
    op.drop_table('one_minute_share')
    op.drop_table('transaction')
    op.drop_table('blob')
    ### end Alembic commands ###
