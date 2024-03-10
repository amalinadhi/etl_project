"""Class for check table"""

import sqlalchemy

from src.load.session import BaseSesssion
from src.load.create import UpdateLog


def table_names(engine):
    """Get the table names"""
    table_names = (
        sqlalchemy.inspect(engine)
        .get_table_names()
    )

    return table_names

def latest_row(engine, table_name):
    """Get the latest row of loading a table"""
    # Create session
    session = BaseSesssion()
    session.create_from(engine)

    # Query
    results = (
        session.session.query(UpdateLog)                    # Select the update_log table
        .where(UpdateLog.table_name == table_name)  # Where table_name = table_name
        .order_by(UpdateLog.updated_at.desc())      # Order by updated_at in descending order
    ).all()

    # Check whether we have ever load the table_name
    if len(results) == 0:
        # It means we have yet load the table_name
        last_row = 0
    else:
        last_row = results[0].last_row

    return last_row
