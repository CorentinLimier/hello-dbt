"""create test table

Revision ID: 5b40825f2595
Revises: 
Create Date: 2022-03-05 11:53:41.323014

"""
from datetime import date

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '5b40825f2595'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    game_table = op.create_table(
        'games',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
    )
    op.bulk_insert(game_table,
        [
            {'id': 1, 'name': 'Powl'},
            {'id': 2, 'name': 'Flappy Angry Bird'},
            {'id': 3, 'name': 'Tower Ranger'}
        ]
    )
    downloads_table = op.create_table(
        'downloads',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('id_game', sa.Integer, sa.ForeignKey('games.id'), nullable=False),
        sa.Column('downloaded_at', sa.Date, nullable=False),
    )
    op.bulk_insert(downloads_table,
        [
            {'id': 1, 'id_game': 1, 'downloaded_at': date(2010, 10, 5)},
            {'id': 2, 'id_game': 1, 'downloaded_at': date(2007, 5, 27)},
            {'id': 3, 'id_game': 1, 'downloaded_at': date(2008, 8, 15)},
            {'id': 4, 'id_game': 2, 'downloaded_at': date(2012, 9, 4)},
            {'id': 5, 'id_game': 3, 'downloaded_at': date(2007, 5, 1)},
            {'id': 6, 'id_game': 3, 'downloaded_at': date(2011, 4, 3)},
        ]
    )

def downgrade():
    op.drop_table('downloads')
    op.drop_table('games')
