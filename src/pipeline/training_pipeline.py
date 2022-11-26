import sys, os
from src.exception import GeoException
from src.logger import logging
from src.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact
from src.components.data_ingestion import DataIngestion

class TrainPipeline:
    def __init__(self,):
        self.training_pipeline_config = TrainingPipelineConfig()
        self.data_ingestion_config = DataIngestionConfig(
                    training_pipeline_config=self.training_pipeline_config)

    def start_data_ingestion(self,)->DataIngestionArtifact:
        try:
            logging.info("Starting Data Ingestion!")

            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)

            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()

            logging.info(f"Data Ingestion Completed. Artifact {data_ingestion_artifact}")
            
            return data_ingestion_artifact

        except Exception as e:
            raise GeoException(e,sys)

    def run_pipeline(self,):
        
        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()

        except Exception as e:
            raise GeoException(e,sys)      