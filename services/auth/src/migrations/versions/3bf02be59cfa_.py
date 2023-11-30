"""empty message

Revision ID: 3bf02be59cfa
Revises: b0f3fbdbcdf1
Create Date: 2023-11-30 14:47:23.126772

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = "3bf02be59cfa"
down_revision = "b0f3fbdbcdf1"
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
        batch_op.drop_constraint("phone_number_user_id_key", type_="unique")
        batch_op.drop_constraint("phone_number_user_id_fkey", type_="foreignkey")
        batch_op.drop_column("user_id")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("phone_number", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True)
        )
        batch_op.create_foreign_key(
            "phone_number_user_id_fkey", "user", ["user_id"], ["id"]
        )
        batch_op.create_unique_constraint("phone_number_user_id_key", ["user_id"])
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
