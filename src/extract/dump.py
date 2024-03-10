"""Load data source"""

import joblib
import pandas as pd

from src.util import logging


def to_pickle(data: pd.DataFrame, filepath: str) -> None:
    """
    Dump data to a .pkl file

    Parameters
    ----------
    data : pd.DataFrame
        The data you want to dump

    filepath : str
        The file path
    """
    try:
        joblib.dump(data, filepath)
        logging.print_debug(f"Successfuly dump the data to {filepath}!")

    except Exception as error:
        raise RuntimeError("Path is invalid")
    
def to_csv(data: pd.DataFrame, filepath: str, return_index: bool=False) -> None:
    """
    Dump data to a .csv file

    Parameters
    ----------
    data : pd.DataFrame
        The data you want to dump

    filepath : str
        The file path

    return_index : bool, default=False
        Whether to return index or not
    """
    try:
        data.to_csv(filepath, index=return_index)
        logging.print_debug(f"Successfuly dump the data to {filepath}!")

    except Exception as error:
        raise RuntimeError("Path is invalid")
