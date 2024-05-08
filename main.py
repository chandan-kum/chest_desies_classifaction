from src.chest_des_clasf import logger

from src.chest_des_clasf.pipeline.stage_01_data_ingedtion import DataIngestionTrainingPipeline

STAGE_NAME = "data ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nX========X") 
except Exception as e:
    logger.exception(e)
    raise e