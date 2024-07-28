from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline
  
  
import dagshub
dagshub.init(repo_owner='chikien729', repo_name='e2eMLE-tutor', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)


STAGE_NAME = "Data Ingestion stage"
try: 
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"

try: 
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"

try: 
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    model_training = ModelTrainingPipeline()
    model_training.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Evaluation"

try: 
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e
