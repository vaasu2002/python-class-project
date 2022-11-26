import os

TARGET_COLUMN = "class"
PIPELINE_NAME: str = "Geochemical_Classification"
ARTIFACT_DIR: str = "artifact"

"""
constants related to Data Ingestion components
"""
FILE_NAME: str = "GeochemicalData.csv"

TRAIN_FILE_NAME: str = "train.csv"

TEST_FILE_NAME: str = "test.csv"

DATA_INGESTION_COLLECTION_NAME: str = "chromitite_layer_data"

DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_INGESTION_INGESTED_DIR: str = "ingested"

DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2
