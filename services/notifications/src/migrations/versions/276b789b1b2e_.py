"""empty message

Revision ID: 276b789b1b2e
Revises: 20701f8065c2
Create Date: 2023-12-06 14:59:19.979544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '276b789b1b2e'
down_revision = '20701f8065c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_notification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('is_sent', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('email_notification')
    # ### end Alembic commands ###
