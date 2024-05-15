# Chicken-Disease-Classification

## Workflows
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml

## How to run?

STEPS:

#### Clone the repository

```
https://github.com/rrrreddy/Chicken-Disease-Classification.git
```
#### Create a conda environment

```
conda create -n cdc python=3.7 -y
```
#### Activate the environment

```
conda activate cdc
```
#### Install the dependencies

```
pip install -r requirements.txt
```

# Finally run the following command
python app.py
Now,

open up you local host and port

### DVC cmd

```
dvc init
```

```
dvc repro
```

```
dvc dag
```


## AZURE-CICD-Deployment-with-Github-Actions

#### Save pass:
```
s3cEZKH5yytiVnJ3h+eI3qhhzf9q1vNwEi6+q+WGdd+ACRCZ7JD6
```

#### Run from terminal:
docker build -t chickenapp.azurecr.io/chicken:latest .

docker login chickenapp.azurecr.io

docker push chickenapp.azurecr.io/chicken:latest

#### Deployment steps

Build the Docker image of the Source Code
Push the Docker image to Container Registry
Launch the Web App Server in Azure
Pull the Docker image from the container registry to Web App server and run



