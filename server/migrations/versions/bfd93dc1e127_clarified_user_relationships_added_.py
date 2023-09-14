"""Clarified user relationships, added table names for prompts.

Revision ID: bfd93dc1e127
Revises: 37d5df6182f9
Create Date: 2023-09-14 11:55:35.909941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfd93dc1e127'
down_revision = '37d5df6182f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('career_prompts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prompt', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('relationship_prompts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prompt', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('self_growth_prompts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prompt', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('career_journal_prompt')
    op.drop_table('relationship_journal_prompt')
    op.drop_table('self_growth_journal_prompt')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('self_growth_journal_prompt',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('prompt', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('relationship_journal_prompt',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('prompt', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('career_journal_prompt',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('prompt', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('self_growth_prompts')
    op.drop_table('relationship_prompts')
    op.drop_table('career_prompts')
    # ### end Alembic commands ###