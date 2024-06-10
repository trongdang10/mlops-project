import os
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger

STAGE_NAME = "Model evaluation stage"

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/trongdang10/mlops-wine-quality.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="trongdang10"
os.environ["MLFLOW_TRACKING_PASSWORD"]="476952ea6ed76a9d0e04ada75e4f70e65638702a"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

