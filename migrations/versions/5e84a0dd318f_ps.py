"""ps

Revision ID: 5e84a0dd318f
Revises: 537547987ae9
Create Date: 2018-07-24 21:23:17.353981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e84a0dd318f'
down_revision = '537547987ae9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('aim', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'aim')
    # ### end Alembic commands ###
