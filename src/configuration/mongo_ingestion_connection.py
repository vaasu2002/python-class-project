import pymongo
from src.constant.database import INGESTION_DATABASE_NAME,INGESTION_COLLECTION_NAME,MONGO_URL

class MongoDBClient:
    def __init__(self,database_name=INGESTION_DATABASE_NAME,collections_name=INGESTION_COLLECTION_NAME) -> None:
        try:
            self.client = pymongo.MongoClient(MONGO_URL)
            self.database_name = database_name
            self.collections_name = collections_name
        
        except Exception as e:
            raise e