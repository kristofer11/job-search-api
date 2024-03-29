"""add index to applications(user_id) in models.py

Revision ID: 09426a6f3c95
Revises: b4ff1767b79c
Create Date: 2024-01-10 23:09:03.800368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09426a6f3c95'
down_revision = 'b4ff1767b79c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_applications_user_id'), 'applications', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_applications_user_id'), table_name='applications')
    # ### end Alembic commands ###
