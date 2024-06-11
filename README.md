# mlops-project

## Workflows

My workflows will look like this:
1. create setuptools in setup.py, which makes it easier when calling dependencies from ./src
2. create logging in ./src/mlProject/__init__.py, so that everytime a .py file is executed, it will be listed in /logs file, this makes the tracking process easier
3. create some functions in src\mlProject\utils\common.py that will be reused during the project
4. given following files, create a constants __init__.py in src\mlProject\utils\common.py that will retrive the parameters from schema.yaml, params.yaml, config/config.yaml.
5. Pipeline:
    we have in total 5 pipelines named: 
        - "stage_01_data_ingestion.py", 
        - "stage_02_data_validation.py",
        - "stage_03_data_transformation.py",
        - "stage_04_model_trainer.py",
        - "stage_05_model_evaluation.py"
    In each stage the workflow will be as follows:
    1. Update config\config.yaml
    2. Update schema.yaml
    3. Update params.yaml
    4. Update the src\mlProject\entity\config_entity.py
    5. Update the configuration manager in src\mlProject\config\configuration.py
    6. Update the conponents in src\mlProject\components
    7. Update the pipeline in src\mlProject\pipeline
    8. Update the main.py (which will run all stages in one shot)
6. update prediction.py, which will predict based on a trained model from "stage_04_model_trainer.py".
7. And in the end, everything in app.py, which also performs a prediction on a web app


### DVC tracking Pipeline is displaying in a remote repo on [dagshub](https://dagshub.com/trongdang10/mlops-wine-quality)

# How to run?
##### note: you might need MLflow TOKEN to load a prediction service, which can be regenerated on [dagshub](https://dagshub.com/), details will be highlighed at the end.

### STEP 01- Clone repo, create and activate after  a environment opening the repository
Clone the repository: 
https://github.com/trongdang10/mlops-project

```bash
# assuming you already have an environment
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 03- execute main.py and app.py
```bash
python main.py
```
```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


#### 

## MLflow
[Documentation](https://mlflow.org/docs/latest/index.html)

### dagshub
[dagshub](https://dagshub.com/)

Firstly, you need to have following infors before hand:
MLFLOW_TRACKING_URI=https://dagshub.com/<user-name>/<repo-name>.mlflow \
MLFLOW_TRACKING_USERNAME=<your-user-name> \
MLFLOW_TRACKING_PASSWORD=<your-token> \

Then, run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/<user-name>/<repo-name>.mlflow
export MLFLOW_TRACKING_USERNAME=<your-user-name>
export MLFLOW_TRACKING_PASSWORD=<your-token>
```

After this you export your mlflow credentials, you then can adjust the variable in stage_05_model_evaluation.
