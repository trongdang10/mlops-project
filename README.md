# mlops-project

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity         ### a writen type of functionality
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/trongdang10/mlops-project
```
### STEP 01- Create and activate after  a environment opening the repository

```bash
conda create -n env_name python=3.* -y
```

```bash
conda activate env_name
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/trongdang10/mlops-project.mlflow \
MLFLOW_TRACKING_USERNAME=trongdang10 \
MLFLOW_TRACKING_PASSWORD=HASD123566628999123AA2231 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/trongdang10/mlops-project.mlflow 

export MLFLOW_TRACKING_USERNAME=trongdang10 

export MLFLOW_TRACKING_PASSWORD=HASD123566628999123AA2231

```


## This is a large change