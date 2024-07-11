"""Increased character range for description and added _password_hash column to user table

Revision ID: 926e3505c55f
Revises: 5882978c6532
Create Date: 2024-07-12 00:54:09.709520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '926e3505c55f'
down_revision = '5882978c6532'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.alter_column('carDescription',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=280),
               existing_nullable=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_password_hash', sa.String(length=250), nullable=False))
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=200), autoincrement=False, nullable=False))
        batch_op.drop_column('_password_hash')

    with op.batch_alter_table('car', schema=None) as batch_op:
        batch_op.alter_column('carDescription',
               existing_type=sa.String(length=280),
               type_=sa.VARCHAR(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###

