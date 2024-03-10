"""Base class"""

import pandas as pd

from src.extract.read import from_spreadsheet, from_pickle
from src.extract.dump import to_pickle, to_csv


class BaseSource:
    """Base source class."""
    # Extract methods
    def extract_spreadsheet(self, sheet_id, sheet_name):
        return from_spreadsheet(sheet_id, sheet_name)
    
    def extract_pickle(self, filepath):
        return from_pickle(filepath)

    # Dump methods
    def dump_pickle(self, data, filepath):
        to_pickle(data=data, filepath=filepath)

    def dump_csv(self, data, filepath, return_index=False):
        to_csv(data=data, filepath=filepath, return_index=return_index)

class BaseSourceGoogleSheet(BaseSource):
    """Base source class from Google Sheet"""
    def __init__(
            self, 
            sheet_id = None,
            sheet_name = None,
            **kwargs):
        if not sheet_id:
            raise Exception('Masukkan Spreadsheet ID')
        
        if not sheet_name:
            raise Exception('Masukkan sheet name')
        
        self.sheet_id = sheet_id
        self.sheet_name = sheet_name
        self.kwargs = kwargs

    def extract(self):
        # Extract data from spreadsheet
        data = self.extract_spreadsheet(self.sheet_id, self.sheet_name)

        # Save as a dataframe
        if 'has_header' in self.kwargs.keys():
            if self.kwargs['has_header'] == False:
                self.data = pd.DataFrame(data)

        else:
            self.data = pd.DataFrame(
                data[1:],
                columns = data[0]
            )
