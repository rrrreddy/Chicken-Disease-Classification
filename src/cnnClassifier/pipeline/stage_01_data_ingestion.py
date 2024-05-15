from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    """
    Data Ingestion Training Pipeline
    """
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.unzip_data()
    
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Starting {STAGE_NAME}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Ending {STAGE_NAME}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME}: {e}")
        raise e

    