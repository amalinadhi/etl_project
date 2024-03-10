
from src.pipeline.iris import IrisPipeline


if __name__ == "__main__":
    # ETL on IRIS data
    iris = IrisPipeline()
    iris.execute()