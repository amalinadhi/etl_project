"""Template for creating table"""

from sqlalchemy import Column
from sqlalchemy import Integer, Float, VARCHAR, DateTime
from sqlalchemy.sql import func

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# IRIS TABLE
class Iris(Base):
    # Define table name
    __tablename__ = "iris"

    # Define columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    sepal_length = Column(Float)
    sepal_width = Column(Float)
    petal_length = Column(Float)
    petal_width = Column(Float)
    target = Column(VARCHAR(80))

    # Define printing object
    def __repr__(self):
        return f"Iris(id={self.id!r}, sepal_length={self.sepal_length!r}, sepal_width={self.sepal_width!r}, petal_length={self.petal_length!r}, petal_width={self.petal_width!r}, target={self.target!r})"


# UPDATE LOG TABLE
class UpdateLog(Base):
    # Define table name
    __tablename__ = "update_log"

    # Define columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
    table_name = Column(VARCHAR(80))
    last_row = Column(Integer)

    # Define printing object
    def __repr__(self):
        return f"UpdateLog(id={self.id!r}, updated_at={self.updated_at!r}, table_name={self.table_name!r}, last_row={self.last_row!r})"


# Function to create table
def create_table(engine, table_class):
    """Create the iris table"""
    table_class.__table__.create(bind=engine, checkfirst=True)
