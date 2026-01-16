## MySQL --->>Train test split --->>Dataset

import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd 



from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str= os.path.join("artifacts", "train.csv")
    test_data_path: str= os.path.join("artifacts", "test.csv")
    raw_data_path: str= os.path.join("artifacts", "raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config= DataIngestionConfig()


    def initiate_data_ingestion(self):
        try:
            #Read the data from mysql database
            logging.info("Reading from Mysql database")
            #After reading the data, save it path in Artifacts Folder
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
        except Exception as e:
            raise CustomException(e, sys)    