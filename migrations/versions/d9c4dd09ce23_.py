"""empty message

Revision ID: d9c4dd09ce23
Revises: 273bc872cf48
Create Date: 2021-05-18 11:31:14.370030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9c4dd09ce23'
down_revision = '273bc872cf48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('phone', sa.String(), nullable=True))
    op.drop_column('customer', 'phone_num')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('phone_num', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('customer', 'phone')
    # ### end Alembic commands ###