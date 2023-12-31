"""Added relationships

Revision ID: f83e86fd43e6
Revises: 2a68b115b558
Create Date: 2023-09-12 12:58:56.405043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f83e86fd43e6'
down_revision = '2a68b115b558'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('calendar_entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('fk_calendar_entries_user_users', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_calendar_entries_user_id_users'), 'users', ['user_id'], ['id'])
        batch_op.drop_column('user')

    with op.batch_alter_table('journal_entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('fk_journal_entries_user_users', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_journal_entries_user_id_users'), 'users', ['user_id'], ['id'])
        batch_op.drop_column('user')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('journal_entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_journal_entries_user_id_users'), type_='foreignkey')
        batch_op.create_foreign_key('fk_journal_entries_user_users', 'users', ['user'], ['id'])
        batch_op.drop_column('user_id')

    with op.batch_alter_table('calendar_entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_calendar_entries_user_id_users'), type_='foreignkey')
        batch_op.create_foreign_key('fk_calendar_entries_user_users', 'users', ['user'], ['id'])
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
