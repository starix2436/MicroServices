"""empty message

Revision ID: 0671784ab3f0
Revises: 5f57f8f97da7
Create Date: 2023-11-30 13:56:42.968748

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "0671784ab3f0"
down_revision = "5f57f8f97da7"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("phone_number", schema=None) as batch_op:
        batch_op.alter_column(
            "mobile",
            existing_type=sa.VARCHAR(length=20),
            type_=sqlalchemy_utils.types.phone_number.PhoneNumberType(length=10),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "mobile2",
            existing_type=sa.VARCHAR(length=20),
            type_=sqlalchemy_utils.types.phone_number.PhoneNumberType(length=10),
            existing_nullable=True,
        )
        batch_op.alter_column(
            "home",
            existing_type=sa.VARCHAR(length=20),
            type_=sqlalchemy_utils.types.phone_number.PhoneNumberType(length=10),
            existing_nullable=True,
        )
        batch_op.alter_column(
            "office",
            existing_type=sa.VARCHAR(length=20),
            type_=sqlalchemy_utils.types.phone_number.PhoneNumberType(length=10),
            existing_nullable=True,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("phone_number", schema=None) as batch_op:
        batch_op.alter_column(
            "office",
            existing_type=sqlalchemy_utils.types.phone_number.PhoneNumberType(
                length=10
            ),
            type_=sa.VARCHAR(length=20),
            existing_nullable=True,
        )
        batch_op.alter_column(
            "home",
            existing_type=sqlalchemy_utils.types.phone_number.PhoneNumberType(
                length=10
            ),
            type_=sa.VARCHAR(length=20),
            existing_nullable=True,
        )
        batch_op.alter_column(
            "mobile2",
            existing_type=sqlalchemy_utils.types.phone_number.PhoneNumberType(
                length=10
            ),
            type_=sa.VARCHAR(length=20),
            existing_nullable=True,
        )
        batch_op.alter_column(
            "mobile",
            existing_type=sqlalchemy_utils.types.phone_number.PhoneNumberType(
                length=10
            ),
            type_=sa.VARCHAR(length=20),
            existing_nullable=False,
        )

    # ### end Alembic commands ###
