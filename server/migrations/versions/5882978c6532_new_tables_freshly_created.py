"""New Tables Freshly Created

Revision ID: 5882978c6532
Revises: 
Create Date: 2024-07-08 19:26:14.640813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5882978c6532'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('car',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('carImage', sa.String(length=255), nullable=False),
    sa.Column('carMake', sa.String(length=50), nullable=False),
    sa.Column('carName', sa.String(length=50), nullable=False),
    sa.Column('carYear', sa.Integer(), nullable=False),
    sa.Column('carPrice', sa.String(length=50), nullable=False),
    sa.Column('carCategory', sa.String(length=50), nullable=False),
    sa.Column('carMileage', sa.String(length=50), nullable=False),
    sa.Column('carEngine', sa.String(length=50), nullable=False),
    sa.Column('carTransmission', sa.String(length=50), nullable=False),
    sa.Column('carFuel', sa.String(length=50), nullable=False),
    sa.Column('carDescription', sa.String(length=255), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['seller_id'], ['user.id'], name=op.f('fk_car_seller_id_user')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('orderId', sa.String(length=50), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('car_id', sa.Integer(), nullable=False),
    sa.Column('customerName', sa.String(length=50), nullable=False),
    sa.Column('customerContact', sa.String(length=100), nullable=False),
    sa.Column('deliveryAddress', sa.String(length=255), nullable=False),
    sa.Column('orderStatus', sa.String(length=50), nullable=False),
    sa.Column('orderDate', sa.DateTime(), nullable=True),
    sa.Column('paymentMethod', sa.String(length=50), nullable=False),
    sa.Column('additionalNotes', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['car_id'], ['car.id'], name=op.f('fk_order_car_id_car')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_order_user_id_user')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('car')
    op.drop_table('user')
    # ### end Alembic commands ###
