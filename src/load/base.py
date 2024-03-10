"""Base class for loading data to a database"""

from src.extract import read
from src.util.database import connect_warehouse
from src.util.logging import print_debug

from src.load import check
from src.load import session
from src.load import create


class BaseLoad:
    """Base class to load a data to database"""
    def __init__(self, table_name, table_obj):
        # Initialize
        self.TABLE_LOG_NAME = 'update_log'
        self.TABLE_LOG_OBJ = create.UpdateLog

        self.TABLE_NAME = table_name
        self.TABLE_OBJ = table_obj

        self.need_update = True

        self.initialize()

    def initialize(self):
        """
        Create the engine, then validate the table
        """
        # Create engine & session
        self.create_engine()
        self.create_session()

        # Get the table names
        self.get_table_names()

        # Create table if not exist
        if self.TABLE_NAME not in self.table_names:
            # Buat table
            self.create_table()

        if self.TABLE_LOG_NAME not in self.table_names:
            # Buat table
            self.create_updatelog_table()

    
    # Initialization
    def create_engine(self):
        """Create engine to connect to a warehouse"""
        self.engine = connect_warehouse()

    def create_session(self):
        """Create a session"""
        self.sess_obj = session.BaseSesssion()
        self.sess_obj.create_from(engine = self.engine)

    def create_table(self):
        """Create the Iris Table"""
        print_debug(f"Create '{self.TABLE_NAME}' table")
        self.TABLE_OBJ.__table__.create(bind = self.engine, checkfirst = True)
        print_debug(f"'{self.TABLE_NAME}' table is created!")

    def create_updatelog_table(self):
        """Create the update log table"""
        print_debug("Create 'update_log' table")
        self.TABLE_LOG_OBJ.__table__.create(bind = self.engine, checkfirst = True)
        print_debug("'update_log' table is created!")

    
    # Get latest info
    def get_latest_row(self):
        """Get the latest row"""
        self.last_row = check.latest_row(engine = self.engine,
                                         table_name = self.TABLE_NAME)
        
    def get_table_names(self):
        """Get all the table names in the database"""
        self.table_names = check.table_names(engine = self.engine)

    
    # Add and commit data
    def add_data(self, data):
        """Load and commit data"""
        self.sess_obj.add(objs = data)

    def add_update_log(self):
        """Add the current proces to the update log"""
        update_obj = self.TABLE_LOG_OBJ(
            table_name = self.TABLE_NAME,
            last_row = self.last_row
        )
        self.add_data(data = [update_obj])

    def commit(self):
        """Commit session"""
        self.sess_obj.commit()

    
    # Extract & load updates
    def extract_csv(self, filepath):
        """Extract data from a specific filepath from .csv file"""
        data = read.from_csv(filepath = filepath)
        return data

    def extract_updates(self, filepath):
        """Extract the update data"""
        # Check whether we have ever update this data
        self.get_latest_row()

        # Extract current data from a filepath
        data = self.extract_csv(filepath)
        data_to_add = data.iloc[self.last_row:]
        self.n_data_to_add = len(data_to_add)

        # Reformat data
        if len(data_to_add) == 0:
            self.need_update = False
        else:
            self.data_to_add_dict = [self.TABLE_OBJ(**row) for key, row in data_to_add.T.to_dict().items()]
            self.last_row = len(data)

    def load_updates(self):
        """Load updates to database"""
        if self.need_update == False:
            print_debug("The data is already up to date!")
        else:
            # Add data that is need to update
            print_debug(f"Add {self.n_data_to_add} data to '{self.TABLE_NAME}' table!")
            self.add_data(data = self.data_to_add_dict)

            # Add update log to update_log table
            print_debug(f"Update the load log!")
            self.add_update_log()

