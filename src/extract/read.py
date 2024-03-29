"""Load data source"""

import joblib
import pandas as pd

from src.credential import google_api
from src.util import logging


def from_pickle(filepath: str) -> list:
    """
    Load data from a given .pkl file

    Parameter
    ---------
    filepath : str
        The pickle file path

    Return
    ------
    data : list
        The read data
    """
    try:
        data = joblib.load(filepath)
        logging.print_debug(f"Successfuly extract data from {filepath}!")

    except FileNotFoundError as error:
        raise RuntimeError("File is not found in path.")

    return data

def from_spreadsheet(sheet_id: str, sheet_name: str) -> list:
    """
    Load spreadsheet values based on sheet_id & sheet_name

    Parameters
    ----------
    sheet_id : str
        The spreadsheet ID

    sheet_name : str
        The sheet name

    Return
    ------
    data : list
        The read data
    """
    # Open the spreadsheet
    sheet = (
        google_api.spreadsheet()    # using the credential,
        .open_by_key(sheet_id)      # open file by spreadsheet id,
        .worksheet(sheet_name)      # then access a specific sheet
    )
    
    data = sheet.get_all_values()
    logging.print_debug(f"Successfuly extract data from {sheet_id}!")

    return data

def from_csv(filepath: str) -> pd.DataFrame:
    """
    Load spreadsheet values based on sheet_id & sheet_name

    Parameters
    ----------
    filepath : str
        The .csv location

    has_header : bool, default=True
        Whether the csv has header or not

    Return
    ------
    data : pd.DataFrame
        the data
    """
    # Open the file
    data = pd.read_csv(filepath)
    logging.print_debug(f"Successfuly extract data from {filepath}!")

    return data

