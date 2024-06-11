# mlops-project

## Workflows

My workflows will proceed as follows:

1. Create `setup.py` using `setuptools`, facilitating easier management of dependencies from `./src`.
2. Implement logging in `./src/mlProject/__init__.py`, ensuring that each executed `.py` file is logged in the `/logs` directory for easier tracking.
3. Develop reusable functions in `src/mlProject/utils/common.py` to be used throughout the project.
4. Create a `constants __init__.py` in `src/mlProject/utils/common.py` to retrieve parameters from `schema.yaml`, `params.yaml`, and `config/config.yaml`.
5. Pipeline process:
    - We have five pipelines named:
        - `stage_01_data_ingestion.py`
        - `stage_02_data_validation.py`
        - `stage_03_data_transformation.py`
        - `stage_04_model_trainer.py`
        - `stage_05_model_evaluation.py`
    - For each stage, the workflow includes:
        1. Updating `config/config.yaml`
        2. Updating `schema.yaml` #__ this will be only in stage_02_04_05
        3. Updating `params.yaml` #__ this will be only in stage_04_05
        4. Updating `src/mlProject/entity/config_entity.py`
        5. Updating the configuration manager in `src/mlProject/config/configuration.py`
        6. Updating components in `src/mlProject/components`
        7. Updating the pipeline in `src/mlProject/pipeline`
        8. Updating `main.py` to run all stages in sequence
    - Along each stage, tracking with DVC will be created. 
6. Update `prediction.py` to make predictions using the trained model from `stage_04_model_trainer.py`.
7. Finally, integrate Training- and Prediction-pipeline into `app.py`, which will perform training and prediction on an web app.
        *note*: `@app.route('/train',methods=['GET'])` will re-execute the training pipeline, which will be used for the prediction.

**General note:** This project does not perform Exploratory Data Analysis because the main purpose is to show the ml traning pipeline and to show its deployment on an web app.

### Tracking Pipeline by DVC and Experiments by MLflow are displaying in a remote repo on [dagshub](https://dagshub.com/trongdang10/mlops-project)

# How to run?
##### Note: You may need an MLflow TOKEN to load a "Prediction Service". This can be regenerated on [dagshub](https://dagshub.com/). Details will be highlighted at the end.


### STEP 01- Clone repo, create and activate a environment after clone and open the repo
Clone the repository: 
https://github.com/trongdang10/mlops-project


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
## DVC
[DVC Documentation](https://dvc.org/doc/start/data-pipelines/data-pipelines)
## MLflow
[MLflow Documentation](https://mlflow.org/docs/latest/index.html)

### dagshub
[dagshub](https://dagshub.com/)

Firstly, you need to have the following infors beforehand:
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
