"""empty message

Revision ID: 7b2736db2df6
Revises: 5935ad734a98
Create Date: 2022-11-11 22:48:53.814783

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7b2736db2df6'
down_revision = '5935ad734a98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('achievement_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('competition_id', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=150), nullable=False),
    sa.Column('match_name', sa.String(length=200), nullable=False),
    sa.Column('match_time', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['competition_id'], ['competition_information.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('achievement_cuber_222', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('achievement_cuber_222_ibfk_2', 'achievement_cuber_222', type_='foreignkey')
    op.drop_constraint('achievement_cuber_222_ibfk_1', 'achievement_cuber_222', type_='foreignkey')
    op.create_foreign_key(None, 'achievement_cuber_222', 'user', ['user_id'], ['id'])
    op.drop_column('achievement_cuber_222', 'uid')
    op.drop_column('achievement_cuber_222', 'cid')
    op.add_column('achievement_cuber_333', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('achievement_cuber_333_ibfk_2', 'achievement_cuber_333', type_='foreignkey')
    op.drop_constraint('achievement_cuber_333_ibfk_1', 'achievement_cuber_333', type_='foreignkey')
    op.create_foreign_key(None, 'achievement_cuber_333', 'user', ['user_id'], ['id'])
    op.drop_column('achievement_cuber_333', 'uid')
    op.drop_column('achievement_cuber_333', 'cid')
    op.add_column('achievement_cuber_oh', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('achievement_cuber_oh_ibfk_1', 'achievement_cuber_oh', type_='foreignkey')
    op.drop_constraint('achievement_cuber_oh_ibfk_2', 'achievement_cuber_oh', type_='foreignkey')
    op.create_foreign_key(None, 'achievement_cuber_oh', 'user', ['user_id'], ['id'])
    op.drop_column('achievement_cuber_oh', 'uid')
    op.drop_column('achievement_cuber_oh', 'cid')
    op.add_column('achievement_cuber_py', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('achievement_cuber_py_ibfk_1', 'achievement_cuber_py', type_='foreignkey')
    op.drop_constraint('achievement_cuber_py_ibfk_2', 'achievement_cuber_py', type_='foreignkey')
    op.create_foreign_key(None, 'achievement_cuber_py', 'user', ['user_id'], ['id'])
    op.drop_column('achievement_cuber_py', 'uid')
    op.drop_column('achievement_cuber_py', 'cid')
    op.add_column('achievement_cuber_sk', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('achievement_cuber_sk_ibfk_1', 'achievement_cuber_sk', type_='foreignkey')
    op.drop_constraint('achievement_cuber_sk_ibfk_2', 'achievement_cuber_sk', type_='foreignkey')
    op.create_foreign_key(None, 'achievement_cuber_sk', 'user', ['user_id'], ['id'])
    op.drop_column('achievement_cuber_sk', 'uid')
    op.drop_column('achievement_cuber_sk', 'cid')
    op.add_column('player_information', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('player_information_ibfk_2', 'player_information', type_='foreignkey')
    op.create_foreign_key(None, 'player_information', 'user', ['user_id'], ['id'])
    op.drop_column('player_information', 'uid')
    op.add_column('user_profile', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('user_profile_ibfk_1', 'user_profile', type_='foreignkey')
    op.create_foreign_key(None, 'user_profile', 'user', ['user_id'], ['id'])
    op.drop_column('user_profile', 'uid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('uid', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'user_profile', type_='foreignkey')
    op.create_foreign_key('user_profile_ibfk_1', 'user_profile', 'user', ['uid'], ['id'])
    op.drop_column('user_profile', 'user_id')
    op.add_column('player_information', sa.Column('uid', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'player_information', type_='foreignkey')
    op.create_foreign_key('player_information_ibfk_2', 'player_information', 'user', ['uid'], ['id'])
    op.drop_column('player_information', 'user_id')
    op.add_column('achievement_cuber_sk', sa.Column('cid', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('achievement_cuber_sk', sa.Column('uid', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'achievement_cuber_sk', type_='foreignkey')
    op.create_foreign_key('achievement_cuber_sk_ibfk_2', 'achievement_cuber_sk', 'user', ['uid'], ['id'])
    op.create_foreign_key('achievement_cuber_sk_ibfk_1', 'achievement_cuber_sk', 'competition_information', ['cid'], ['id'])
    op.drop_column('achievement_cuber_sk', 'user_id')
    op.add_column('achievement_cuber_py', sa.Column('cid', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('achievement_cuber_py', sa.Column('uid', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'achievement_cuber_py', type_='foreignkey')
    op.create_foreign_key('achievement_cuber_py_ibfk_2', 'achievement_cuber_py', 'user', ['uid'], ['id'])
    op.create_foreign_key('achievement_cuber_py_ibfk_1', 'achievement_cuber_py', 'competition_information', ['cid'], ['id'])
    op.drop_column('achievement_cuber_py', 'user_id')
    op.add_column('achievement_cuber_oh', sa.Column('cid', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('achievement_cuber_oh', sa.Column('uid', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'achievement_cuber_oh', type_='foreignkey')
    op.create_foreign_key('achievement_cuber_oh_ibfk_2', 'achievement_cuber_oh', 'user', ['uid'], ['id'])
    op.create_foreign_key('achievement_cuber_oh_ibfk_1', 'achievement_cuber_oh', 'competition_information', ['cid'], ['id'])
    op.drop_column('achievement_cuber_oh', 'user_id')
    op.add_column('achievement_cuber_333', sa.Column('cid', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('achievement_cuber_333', sa.Column('uid', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'achievement_cuber_333', type_='foreignkey')
    op.create_foreign_key('achievement_cuber_333_ibfk_1', 'achievement_cuber_333', 'competition_information', ['cid'], ['id'])
    op.create_foreign_key('achievement_cuber_333_ibfk_2', 'achievement_cuber_333', 'user', ['uid'], ['id'])
    op.drop_column('achievement_cuber_333', 'user_id')
    op.add_column('achievement_cuber_222', sa.Column('cid', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('achievement_cuber_222', sa.Column('uid', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'achievement_cuber_222', type_='foreignkey')
    op.create_foreign_key('achievement_cuber_222_ibfk_1', 'achievement_cuber_222', 'competition_information', ['cid'], ['id'])
    op.create_foreign_key('achievement_cuber_222_ibfk_2', 'achievement_cuber_222', 'user', ['uid'], ['id'])
    op.drop_column('achievement_cuber_222', 'user_id')
    op.drop_table('achievement_table')
    # ### end Alembic commands ###
