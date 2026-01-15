from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys



if __name__ == "__main__":
    logging.info("Starting the application")

    try:
        logging.info("Starting the application")
    except Exception as e:
        logging.info(e)
        raise CustomException(e, sys)
