"""Base class for data pipeline"""

import os
from dotenv import load_dotenv
load_dotenv()

from src.extract.base import BaseSourceGoogleSheet
from src.util.logging import print_debug


# Global Variables
RAW_PATH = os.getenv('RAW_PATH')
INTERIM_PATH = os.getenv('INTERIM_PATH')
PROCESSED_PATH = os.getenv('PROCESSED_PATH')


class BasePipeline:

    def __init__(self):
        pass

    def extract(self):
        """Extract the data from google spreadsheet"""
        obj = BaseSourceGoogleSheet(sheet_id = self.sheet_id,
                                    sheet_name = self.sheet_name)
        obj.extract()
        obj.dump_csv(data = obj.data,
                     filepath = RAW_PATH + self.filename)
        
    def load(self):
        """Load the data to a database"""
        obj = self.BaseLoadData()
        obj.extract_updates(filepath = INTERIM_PATH + self.filename)
        obj.load_updates()
        obj.commit()

    def transform(self):
        """Transform the data"""
        obj = self.BaseTransformData()
        obj.read_updates(filepath = RAW_PATH + self.filename)
        obj.transform()
        obj.dump_csv(data = obj.data,
                     filepath = INTERIM_PATH + self.filename)

    def execute(self):
        """Execute the pipeline"""
        print_debug('START EXTRACTING DATA')
        self.extract()
        print("")

        print_debug('START TRANSFORMING DATA')
        self.transform()
        print("")

        print_debug('START LOADING DATA')
        self.load()
        print("")
