"""Transform class for iris"""

from src.transform.base import BaseTransform
from src.transform import sepal_length


class IrisTransform(BaseTransform):
    def read_updates(self, filepath):
        """Read the updated data"""
        self.data = self.read_csv(filepath=filepath)

    def clean_sepal_length(self):
        """Clean the sepal length"""
        self.data['sepal_length'] = self.data['sepal_length'].apply(sepal_length.clean)

    def transform(self):
        """Transform the data"""
        self.clean_sepal_length()
