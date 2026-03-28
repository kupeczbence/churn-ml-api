# Customer Churn Prediction API (Docker + Cloud Deployment)

This project demonstrates an end-to-end machine learning deployment pipeline, from data preprocessing and model training to containerization and cloud deployment.

The application exposes a REST API that predicts whether a customer is likely to churn based on usage and billing features.

---

# Live Demo

API documentation (Swagger UI):

https://churn-api.onrender.com/docs

https://churn-api-a9qg.onrender.com/docs

You can test the model directly in your browser using interactive requests.

---

# Project Overview

This project covers the full machine learning lifecycle:

* Data preprocessing
* Model training and evaluation
* Model persistence
* REST API for inference
* Docker containerization
* Cloud deployment using Render

---

# Tech Stack

## Machine Learning

* Python
* scikit-learn
* pandas
* numpy

## API

* FastAPI
* Uvicorn

## Deployment & DevOps

* Docker
* Git & GitHub
* Render (cloud hosting)

---

# Repository Structure

```
Deployment_MLOps/
│
├── app/
│   └── main.py              # FastAPI application
│
├── model/
│   ├── churn_model.joblib   # Trained model
│   └── feature_columns.joblib
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── train_and_save_model.py  # Model training script
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

---

# Dataset

The project uses the Telco Customer Churn dataset.

If the dataset is not included in the repository due to size constraints, download it from Kaggle and place it into:

```
data/WA_Fn-UseC_-Telco-Customer-Churn.csv
```

---

# Local Development

## 1. Create virtual environment

```
python -m venv myenv
myenv\Scripts\activate
```

## 2. Install dependencies

```
pip install -r requirements.txt 
```

## 3. Train the model

```
python train_and_save_model.py
```

This generates:

```
model/churn_model.joblib
model/feature_columns.joblib
```

---

# Running the API locally

```
uvicorn app.main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

# Docker Setup

## Check Docker Version
```
docker --version
```

```
Docker version 29.3.1
```
## Check if it runs in the background if not you should start the Docker app in windows
```
docker ps
```
### If it runs you should get this in the terminal:
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
## Build Docker image

```
docker build -t churn-api .
```

## Run container

```
docker run -p 8000:8000 churn-api
```

API will be available at:

```
http://localhost:8000/docs
```

---

# Dockerfile Explanation

The Dockerfile:

* Uses a slim Python base image
* Copies the project files
* Installs dependencies
* Starts the FastAPI server with Uvicorn

This ensures the application runs consistently across environments.

---

# Git Setup

To initialize the repository:

```
git init
git add .
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git commit -m "Initial commit"
git remote add origin https://github.com/username/churn-api.git
git branch -M main
git push -u origin main
```

---

# Cloud Deployment (Render)

The project is deployed using Render's free web service.

Deployment steps:

1. Push the repository to GitHub
2. Create a new Web Service on Render
3. Select Docker as environment
4. Connect the GitHub repository
5. Deploy

Render automatically:

* builds the Docker image
* starts the container
* exposes a public HTTPS endpoint

---

# API Usage Example

POST request to:

```
/predict
```

Example input:

```
{
  "tenure": 2,
  "MonthlyCharges": 10,
  "TotalCharges": 30
}
```

Example response:

```
{
  "churn_probability": 0.385,
  "prediction": "Stayed"
}
```

---

# Key Features

* End-to-end ML pipeline
* REST API for real-time inference
* Containerized deployment
* Public cloud endpoint
* Interactive Swagger documentation

---

## Author

- LinkedIn: www.linkedin.com/in/bence-kupecz-119701305
- GitHub: https://github.com/kupeczbence
