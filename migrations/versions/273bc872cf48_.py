"""empty message

Revision ID: 273bc872cf48
Revises: 
Create Date: 2021-05-17 22:36:09.399710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '273bc872cf48'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('customer_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('postal_code', sa.Integer(), nullable=True),
    sa.Column('phone_num', sa.Integer(), nullable=True),
    sa.Column('register_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('customer_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customer')
    # ### end Alembic commands ###
