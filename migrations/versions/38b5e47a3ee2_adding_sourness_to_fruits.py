"""adding sourness to fruits

Revision ID: 38b5e47a3ee2
Revises: 5f31c6789558
Create Date: 2017-11-28 13:59:12.754432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38b5e47a3ee2'
down_revision = '5f31c6789558'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fruits', sa.Column('sourness', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('fruits', 'sourness')
    # ### end Alembic commands ###
