"""empty message

Revision ID: 583d721ed58a
Revises: ba0f2761e691
Create Date: 2021-04-21 16:37:09.973177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '583d721ed58a'
down_revision = 'ba0f2761e691'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mission_users', sa.Column('missionID', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mission_users', 'missionID')
    # ### end Alembic commands ###