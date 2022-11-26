import sys
import numpy as np
import pandas as pd
from src.configuration.mongo_ingestion_connection import MongoDBClient
from src.constant.database import INGESTION_DATABASE_NAME,INGESTION_COLLECTION_NAME
from src.exception import GeoException

class GeochemicalData:

    def export_collection_as_dataframe(self,database_name:str,collection_name:str)->pd.DataFrame:
        try:
            mongo_client = MongoDBClient(database_name=INGESTION_DATABASE_NAME,
                                              collections_name=INGESTION_COLLECTION_NAME)
            
            db = mongo_client.client[mongo_client.database_name]
            collection = db[mongo_client.collections_name]
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na": np.nan}, inplace=True)
            return df

        except Exception as e:
            raise GeoException(e, sys)
