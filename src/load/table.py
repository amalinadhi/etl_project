"""Update value inside table"""

from src.load.session import BaseSesssion
from src.util.logging import print_debug


def insert(data, table, engine):
    """insert data to a table"""
    # Create session
    session = BaseSesssion()
    session.create_from(engine)

    # Add and commit
    session.bulk_save_objects(data)
    session.commit()
    print_debug(f"Successfully add {data} to {table.__tablename__}!")

