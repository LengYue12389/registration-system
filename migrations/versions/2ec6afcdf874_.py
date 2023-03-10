"""empty message

Revision ID: 2ec6afcdf874
Revises: fed688f7a8e4
Create Date: 2022-11-16 21:20:53.992499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ec6afcdf874'
down_revision = 'fed688f7a8e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_confidentiality',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('confidentiality_question', sa.Text(), nullable=True),
    sa.Column('confidentiality_answer', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_confidentiality')
    # ### end Alembic commands ###
