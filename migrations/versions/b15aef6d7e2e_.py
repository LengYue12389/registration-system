"""empty message

Revision ID: b15aef6d7e2e
Revises: 78e34e08e148
Create Date: 2022-11-20 16:16:54.040050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b15aef6d7e2e'
down_revision = '78e34e08e148'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('achievement_cuber_222', sa.Column('match_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'achievement_cuber_222', 'competition_information', ['match_id'], ['id'])
    op.add_column('achievement_cuber_333', sa.Column('match_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'achievement_cuber_333', 'competition_information', ['match_id'], ['id'])
    op.add_column('achievement_cuber_oh', sa.Column('match_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'achievement_cuber_oh', 'competition_information', ['match_id'], ['id'])
    op.add_column('achievement_cuber_py', sa.Column('match_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'achievement_cuber_py', 'competition_information', ['match_id'], ['id'])
    op.add_column('achievement_cuber_sk', sa.Column('match_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'achievement_cuber_sk', 'competition_information', ['match_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'achievement_cuber_sk', type_='foreignkey')
    op.drop_column('achievement_cuber_sk', 'match_id')
    op.drop_constraint(None, 'achievement_cuber_py', type_='foreignkey')
    op.drop_column('achievement_cuber_py', 'match_id')
    op.drop_constraint(None, 'achievement_cuber_oh', type_='foreignkey')
    op.drop_column('achievement_cuber_oh', 'match_id')
    op.drop_constraint(None, 'achievement_cuber_333', type_='foreignkey')
    op.drop_column('achievement_cuber_333', 'match_id')
    op.drop_constraint(None, 'achievement_cuber_222', type_='foreignkey')
    op.drop_column('achievement_cuber_222', 'match_id')
    # ### end Alembic commands ###
