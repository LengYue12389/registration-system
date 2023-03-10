"""empty message

Revision ID: 89431e7f3323
Revises: 
Create Date: 2022-10-11 21:14:00.818707

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89431e7f3323'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('competition_information',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('match_time', sa.Date(), nullable=False),
    sa.Column('address', sa.String(length=150), nullable=False),
    sa.Column('number_of_applicants', sa.String(length=4), nullable=False),
    sa.Column('project_opening', sa.String(length=500), nullable=False),
    sa.Column('match_name', sa.String(length=200), nullable=False),
    sa.Column('registration_fee', sa.String(length=4), nullable=True),
    sa.Column('registration_end_time', sa.Date(), nullable=False),
    sa.Column('details', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('oder_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('oder_id', sa.Integer(), nullable=True),
    sa.Column('add_time', sa.DateTime(), nullable=True),
    sa.Column('amount', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('add_time')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=150), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('is_super', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('username')
    )
    op.create_table('home_banner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_route', sa.Text(), nullable=True),
    sa.Column('add_time', sa.Date(), nullable=True),
    sa.Column('index', sa.Integer(), nullable=True),
    sa.Column('match_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['match_id'], ['competition_information.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('player_information',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=5), nullable=False),
    sa.Column('mobile', sa.String(length=11), nullable=False),
    sa.Column('age', sa.String(length=3), nullable=False),
    sa.Column('registration_items', sa.String(length=50), nullable=False),
    sa.Column('match_id', sa.Integer(), nullable=True),
    sa.Column('add_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['match_id'], ['competition_information.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player_information')
    op.drop_table('home_banner')
    op.drop_table('user')
    op.drop_table('oder_info')
    op.drop_table('competition_information')
    # ### end Alembic commands ###
