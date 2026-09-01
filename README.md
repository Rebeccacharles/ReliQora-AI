# ReliQora-AI
AI-powered predictive application failure detection using machine learning and deep learning.

### Predictive Application Intelligence

ReliQora AI is an AI-powered application reliability system designed to predict the risk of application failure before it occurs.

The system analyzes application and infrastructure telemetry such as CPU utilization, memory usage, request rate, response latency, error rate, network latency, and active connections to identify patterns associated with potential application failures.

The project combines traditional machine learning and deep learning to estimate application failure probability and provide an interpretable risk assessment.

> **ReliQora** is a project-defined name inspired by **Reliability + Intelligence + Predictive Awareness**.

## Problem Statement

Application failures can be preceded by changes in system and application telemetry such as increasing latency, rising error rates, resource pressure, or abnormal request patterns.

ReliQora AI aims to answer:

**Can application telemetry be used to predict whether an application is at risk of failure before the failure occurs?**

## Objective

Build a predictive AI system that:

* Analyzes application telemetry
* Detects patterns associated with failure
* Predicts application failure risk
* Estimates failure probability
* Identifies important risk indicators
* Provides a real-time-style monitoring dashboard

## Planned Workflow

```text
Application Telemetry
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
Baseline ML Models
        ↓
Deep Learning Model
        ↓
Failure Risk Prediction
        ↓
Explainability
        ↓
Monitoring Dashboard
```

## Key Telemetry Features

* CPU Utilization
* Memory Utilization
* Disk Utilization
* Request Rate
* Response Latency
* Error Rate
* Network Latency
* Active Connections

## Models

### Baseline Models

* Logistic Regression
* Decision Tree
* Random Forest

### Deep Learning

Artificial Neural Network:

```text
Input Features
      ↓
Dense Layer (64)
      ↓
Dropout
      ↓
Dense Layer (32)
      ↓
Dropout
      ↓
Output Layer (Sigmoid)
```

## Evaluation Metrics

The project will evaluate models using:

* Precision
* Recall
* F1-Score
* PR-AUC
* Confusion Matrix

Accuracy alone will not be treated as the primary metric because failing to identify an application that is genuinely at risk can be more costly than generating a false alert.

## Dashboard

The planned dashboard will display:

* Current telemetry
* Failure probability
* Risk level
* Key risk indicators
* Historical trends
* Model predictions

## Technology Stack

**Programming:** Python

**Machine Learning:** Scikit-learn

**Deep Learning:** TensorFlow / Keras

**Data Processing:** Pandas, NumPy

**Visualization:** Matplotlib, Seaborn

**Dashboard:** Streamlit

**Version Control:** Git & GitHub

## Project Status

🚧 Currently under development.

The first version focuses on building the complete machine learning pipeline from data preprocessing to predictive failure-risk visualization.

## Future Enhancements

* Explainable AI using SHAP
* Anomaly detection
* FastAPI prediction service
* Docker deployment
* MLflow experiment tracking
* Real telemetry ingestion
* OpenTelemetry integration
* Cloud deployment
* Intelligent alert generation
* GenAI-based prediction explanations

## Disclaimer

This is an independent learning and portfolio project inspired by real-world application monitoring and AIOps use cases. The project uses publicly available or independently generated data and does not contain proprietary, confidential, or personally identifiable information.


## Author

**Rebecca Charles**

