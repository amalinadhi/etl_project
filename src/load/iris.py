"""Load class for iris table"""


from src.load import create
from src.load.base import BaseLoad


class BaseLoadIris(BaseLoad):

    def __init__(self):
        super().__init__(
            table_name = 'iris',
            table_obj = create.Iris
        )