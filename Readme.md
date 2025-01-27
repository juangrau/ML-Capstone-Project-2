# Data Talks Club - Machine Learning Zoomcamp
# Capstone Project 2

## Cardiology Unit Admission

### Introduction

In the wake of the COVID-19 pandemic, the global healthcare system has faced unprecedented challenges, highlighting the critical need for efficient resource management. One of the key areas where improvements can significantly impact patient care and operational efficiency is the prediction of hospital stay duration. 

This project focuses on developing a machine learning model to predict the number of days a patient might need to stay in the hospital, specifically within a cardiology unit. By leveraging the dataset available on Kaggle, which includes comprehensive patient information and admission details, we aim to create a predictive model that can accurately estimate the length of stay for cardiology patients. This capability is not only crucial for optimizing bed allocation and staffing but also for ensuring that resources are distributed effectively, thereby enhancing the overall quality of care. In a post-pandemic world, such predictive tools can play a pivotal role in preparing healthcare systems for future crises and ensuring sustainable, high-quality patient care.

### Core objective of this project

1. **Data aquisition and preparation**. For this project, I'm using the Cardiology Unit Admission dataset. The dataset contains detailed records of hospital admissions and discharges. It includes information about the type of admission, source of shift, patient demographics, diagnosis, admission and discharge dates, length of stay, and consulting doctors. A more detailed description of this dataset can be found [here]('https://www.kaggle.com/datasets/mansoorahmad4477/cardiology-unit-admission')

2. **Model Selection**. In this case I'll use different Regression ML models and select the best for the job. As the framework for training and tunning the model I'll use Scikit-Learn.

3. **Model Training and Tunning**. Additional to feature engineering we'll use parameters alpha to tune our model.

4. **Prediction**. Utilize the trained model to predict the number of days a patient will stay at the cardioly unit.

5. **Containerization**. To be able to reproduce this result, the model will be placed on a Docker container. 

6. **Model deployment**. Finally, now that the model was placed on a Docker container, the last step of the project will be to setup a serverless deployment environment on AWS and run the project from there.


### Availabe files on the repository

| **File** | **Description** |
| --- | --- |
| Dockerfile | Docker container file required to build the image |
| notebook.ipnb | Jupyter Notebook where data loading and Model selection/tunning as performed |
| Pipfile / Pipfile.lock | pipenv environment files required for the Dockerfile in order to create the docker container |
| predict.py | Script that runs the project as a Flask. | 
| request.py | Script that simulates a request to the Flask service | 
| ridge_regression_model_v1.pkl | Pickle file with the model | 
| train.py | A separate script that train and saves the model |
| data | folder with the data used on this project |
| serverless | Directory with the files created to deploy the model on AWS Lambda Function |
| requirements.txt | all libraries required |

### How to run this project

1. Download all the files or clone this repository on your system. To clone the repo, you can execute the following command from the shell:

```sh
git clone https://github.com/juangrau/ML-Capstone-Project-2.git
```

2. Navigate to the project directory on your terminal.
  
3. build and run the docker image:
  

```sh
docker build -t admission .

docker run -it -p 9696:9696 admission:latest
```

The scope of this image is a web service based on Flask that allows to predict if a tele-marketing campaign will be successful for a customer of a bank.

To test it you can run the script request.py like this:

```sh
python request.py
```

Make sure you have the requests library installed. To install it you can run the follwing command on the terminal

```sh
pip install requirements.txt
```

### AWS Lambda Deployment

As described on the table above there the **serverless** directory contains all the files required to deploy the project as a AWS Lambda function.

The lambda function was deployed using a Docker container.

To test this container you can follow these steps:

1. Navigate to the project directory on your terminal.

2. build and run the docker image:

```sh
docker build -t admission-imageaws .

docker run -it -p 8080:8080 admission-imageaws:latest
```

To test it you can run the script test.py like this:

```sh
python test.py
```

The bad news is that I wan't able to get a successful local test. I'm guessing it has something to do with the scikit-learn library available on aws.

In the case of tensorflow, on the course it was provided a wheel file to solve this, so I'll need to update this project in the near future to solve this aspect.