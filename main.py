import os,sys
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from src.data_access.geochemical_data import GeochemicalData
from src.constant.database import INGESTION_DATABASE_NAME,INGESTION_COLLECTION_NAME

data = GeochemicalData()

dataframe = data.export_collection_as_dataframe(database_name=INGESTION_DATABASE_NAME, collection_name=INGESTION_COLLECTION_NAME)
print(dataframe.shape)