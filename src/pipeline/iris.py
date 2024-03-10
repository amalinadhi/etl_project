import os
from dotenv import load_dotenv
load_dotenv()

from src.pipeline.base import BasePipeline
from src.transform.iris import IrisTransform
from src.load.iris import BaseLoadIris



# Global variables
SOURCE_IRIS_SHEET_ID = os.getenv('SOURCE_IRIS_SHEET_ID')
SOURCE_IRIS_SHEET_NAME = os.getenv('SOURCE_IRIS_SHEET_NAME')


class IrisPipeline(BasePipeline):
    sheet_id = SOURCE_IRIS_SHEET_ID
    sheet_name = SOURCE_IRIS_SHEET_NAME
    filename = 'iris.csv'
    BaseLoadData = BaseLoadIris
    BaseTransformData = IrisTransform

    def __init__(self):
        super().__init__()

