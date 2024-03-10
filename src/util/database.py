import os

from sqlalchemy import URL
from sqlalchemy import create_engine

from dotenv import load_dotenv
load_dotenv()


# GLOBAL VARIABLES
WAREHOUSE_DB_USERNAME = os.getenv("WAREHOUSE_DB_USERNAME")
WAREHOUSE_DB_PASSWORD = os.getenv("WAREHOUSE_DB_PASSWORD")
WAREHOUSE_DB_HOST = os.getenv("WAREHOUSE_DB_HOST")
WAREHOUSE_DB_PORT = os.getenv("WAREHOUSE_DB_PORT")
WAREHOUSE_DB_NAME = os.getenv("WAREHOUSE_DB_NAME")


def connect_warehouse():
    """Connect to the warehouse database"""
    # Create url
    url_object = URL.create(
        "postgresql",
        username = WAREHOUSE_DB_USERNAME,
        password = WAREHOUSE_DB_PASSWORD,
        host = WAREHOUSE_DB_HOST,
        port = WAREHOUSE_DB_PORT,
        database = WAREHOUSE_DB_NAME
    )
    engine = create_engine(url_object)

    return engine

