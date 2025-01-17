"""empty message

Revision ID: d8a7d33861c9
Revises: ef9ff3cf446e
Create Date: 2021-05-18 23:25:10.581696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8a7d33861c9'
down_revision = 'ef9ff3cf446e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('title', sa.String(), nullable=True))
    op.drop_column('video', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('video', 'title')
    # ### end Alembic commands ###
