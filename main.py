from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Starting {STAGE_NAME}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Ending {STAGE_NAME}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME}: {e}")
        raise e

STAGE_NAME = "Prepare base model"
