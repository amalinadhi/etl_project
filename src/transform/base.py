"""Base Transform Class"""

from src.extract import read, dump


class BaseTransform:

    def read_csv(self, filepath):
        """Extract data from a specific filepath from .csv file"""
        data = read.from_csv(filepath = filepath)
        return data
    
    def dump_csv(self, data, filepath, return_index=False):
        """dump data to a specific filepath"""
        dump.to_csv(data=data, filepath=filepath, return_index=return_index)

