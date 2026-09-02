# ReliQora-AI

### AI-Powered Predictive Application Failure Detection

ReliQora-AI is a machine learning and deep learning project designed to **predict application failure risk from application and infrastructure telemetry**.

The system analyzes telemetry such as CPU utilization, memory utilization, response latency, error rate, network latency, request rate, and active connections to estimate the probability of application failure.

**Current Release: `v1.0.0` - Initial Release**

---

## Overview

Application failures are often preceded by changes in system and application telemetry.

Increasing resource utilization, higher response latency, rising error rates, network delays, and increasing connection loads can indicate that an application may be approaching an unstable state.

ReliQora-AI explores whether these telemetry signals can be used to **predict application failure risk before an actual failure occurs**.

The project combines:

* Traditional Machine Learning
* Artificial Neural Networks
* Data preprocessing
* Model evaluation
* Failure probability prediction
* Risk-level classification
* Telemetry-based risk indicators
* Interactive Streamlit dashboard

> **ReliQora** is a project-defined name inspired by **Reliability + Intelligence + Predictive Awareness**.

---

## Problem Statement

Application failures can be preceded by measurable changes in application and infrastructure telemetry.

The goal of ReliQora-AI is to answer:

> **Can application telemetry be used to predict whether an application is at risk of failure before the failure occurs?**

---

## Objectives

ReliQora-AI aims to:

* Analyze application telemetry
* Identify patterns associated with application failures
* Predict application failure probability
* Classify application risk levels
* Identify major telemetry-based risk indicators
* Compare traditional ML models with a neural network
* Provide an interactive monitoring-style dashboard

---

## System Workflow

```text
Application Telemetry
        ↓
Data Generation
        ↓
Data Preprocessing
        ↓
Feature Scaling
        ↓
Train/Test Split
        ↓
Baseline ML Models
        ↓
Artificial Neural Network
        ↓
Model Evaluation
        ↓
Best Model Selection
        ↓
Failure Probability Prediction
        ↓
Risk-Level Classification
        ↓
Streamlit Dashboard
```

---

## Telemetry Features

The model uses eight telemetry features:

| Feature            | Description                               |
| ------------------ | ----------------------------------------- |
| CPU Utilization    | Percentage of CPU resources being used    |
| Memory Utilization | Percentage of memory resources being used |
| Disk Utilization   | Percentage of disk resources being used   |
| Request Rate       | Rate of incoming application requests     |
| Response Latency   | Application response time                 |
| Error Rate         | Percentage of failed requests             |
| Network Latency    | Network communication delay               |
| Active Connections | Number of active application connections  |

---

## Machine Learning Models

### Baseline Models

The following classification models were trained and evaluated:

* Logistic Regression
* Decision Tree
* Random Forest

### Deep Learning Model

An Artificial Neural Network was also implemented using TensorFlow/Keras.

```text
Input Features
      ↓
Dense Layer (64 neurons)
      ↓
Dropout (30%)
      ↓
Dense Layer (32 neurons)
      ↓
Dropout (20%)
      ↓
Output Layer (Sigmoid)
```

The ANN contains **2,689 trainable parameters**.

---

## Model Evaluation

Because application failure detection is a classification problem where missed failures can be important, the project evaluates models using:

* Precision
* Recall
* F1-Score
* PR-AUC
* Confusion Matrix

Accuracy is reported for completeness but is **not treated as the primary model-selection metric**.

### V1.0.0 Results

| Model                   | Accuracy | Failure Recall | Failure F1-Score |     PR-AUC |
| ----------------------- | -------: | -------------: | ---------------: | ---------: |
| **Logistic Regression** | **0.76** |       **0.74** |         **0.74** | **0.8186** |
| ANN                     |     0.76 |           0.72 |             0.74 |     0.8185 |
| Random Forest           |     0.75 |           0.73 |             0.74 |     0.8129 |
| Decision Tree           |     0.68 |           0.62 |             0.65 |     0.6821 |

### 🏆 Selected V1.0 Model

**Logistic Regression** was selected as the primary prediction model for the V1.0 dashboard because it achieved the highest PR-AUC:

> **PR-AUC: 0.8186**

The ANN performed almost identically with a PR-AUC of 0.8185, while Random Forest achieved 0.8129.

---

## Logistic Regression Confusion Matrix

The V1.0 Logistic Regression model produced:

```text
[[829 234]
 [244 693]]
```

This corresponds to:

* True Negatives: 829
* False Positives: 234
* False Negatives: 244
* True Positives: 693

The model achieved a **74% recall for the failure class**, meaning it correctly identified a substantial portion of the simulated failure cases.

---

## Interactive Dashboard

ReliQora-AI includes a Streamlit dashboard that allows users to enter telemetry values and receive an application failure-risk prediction.

### Dashboard capabilities

The V1.0 dashboard provides:

* CPU utilization input
* Memory utilization input
* Disk utilization input
* Request rate input
* Response latency input
* Error rate input
* Network latency input
* Active connections input
* Failure probability
* Risk-level classification
* Key risk indicators
* Model identification

### Risk Levels

The dashboard classifies predicted failure probability into three levels:

| Probability  | Risk Level |
| ------------ | ---------- |
| `< 30%`      | 🟢 LOW     |
| `30% – <60%` | 🟡 MEDIUM  |
| `≥ 60%`      | 🔴 HIGH    |

The dashboard also checks telemetry values against predefined thresholds to identify major risk indicators.

---

## Example Prediction

### Normal Telemetry

Using the default dashboard telemetry values, the model produced approximately:

```text
Failure Probability: 2.78%
Risk Level: LOW
```

The dashboard reported:

```text
No major telemetry risk indicators detected.
```

### High-Risk Telemetry

When telemetry was configured with elevated resource usage and latency:

```text
CPU Utilization       → 90%
Memory Utilization    → 90%
Disk Utilization      → 85%
Response Latency      → 700 ms
Error Rate            → 15%
Network Latency       → 200 ms
Active Connections    → 800
```

The model produced:

```text
Failure Probability: 99.11%
Risk Level: HIGH
```

The dashboard identified multiple risk indicators, including:

* High CPU utilization
* High memory utilization
* High disk utilization
* High response latency
* High error rate
* High network latency
* High number of active connections

---

## Technology Stack

### Programming

* Python 3.10+

### Machine Learning

* Scikit-learn

### Deep Learning

* TensorFlow
* Keras

### Data Processing

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Dashboard

* Streamlit

### Model Persistence

* Joblib
* Keras model format

### Version Control

* Git
* GitHub

---

## Project Structure

```text
ReliQora-AI/
│
├── app.py
├── generate_dataset.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── data/
│   ├── raw/
│   │   └── telemetry_data.csv
│   │
│   └── processed/
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       └── y_test.csv
│
├── models/
│   ├── logistic_regression.pkl
│   ├── decision_tree.pkl
│   ├── random_forest.pkl
│   ├── scaler.pkl
│   └── ann_model.keras
│
├── src/
│   ├── preprocess.py
│   ├── train_baseline.py
│   ├── train_models.py
│   └── train_ann.py
│
├── notebooks/
│
└── reports/
    └── figures/
```

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Rebeccacharles/ReliQora-AI.git
cd ReliQora-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Generate the dataset

```bash
python generate_dataset.py
```

### 6. Preprocess the data

```bash
python src/preprocess.py
```

### 7. Train the baseline models

```bash
python src/train_baseline.py
python src/train_models.py
```

### 8. Train the ANN

```bash
python src/train_ann.py
```

### 9. Launch the dashboard

```bash
python -m streamlit run app.py
```

The application will be available locally through the Streamlit URL displayed in the terminal.

---

## V1.0.0 Release

### V1.0.0 - Initial Release

The first release provides an end-to-end predictive application failure detection pipeline:

* Synthetic telemetry dataset
* Data preprocessing
* Feature scaling
* Three baseline ML models
* Artificial Neural Network
* Model evaluation
* Logistic Regression model selection
* Failure probability prediction
* Risk-level classification
* Telemetry risk indicators
* Interactive Streamlit dashboard

**Release:** `v1.0.0`

---

## Current Scope

V1.0.0 uses **independently generated synthetic telemetry data** to demonstrate the machine learning workflow.

The dashboard provides a **real-time-style simulation** rather than a connection to live production telemetry.

The current release is intended as a learning and portfolio implementation of an application reliability prediction workflow.

---

## Future Enhancements

Planned improvements include:

* Explainable AI using SHAP
* Feature-importance visualization
* Historical telemetry trends
* Real telemetry ingestion
* Anomaly detection
* OpenTelemetry integration
* FastAPI prediction service
* Docker containerization
* MLflow experiment tracking
* Cloud deployment
* Automated alert generation
* GenAI-based prediction explanations

---

## 📌 Limitations

* The current dataset is independently generated rather than collected from a production monitoring system.
* Model performance is therefore representative of the generated dataset and should not be interpreted as production performance.
* The V1.0 dashboard uses manually entered telemetry values rather than a live telemetry stream.
* Risk-indicator thresholds in the dashboard are predefined rules and are separate from the machine learning probability prediction.

---

## Disclaimer

This is an independent learning and portfolio project inspired by real-world application monitoring and AIOps use cases.

The project uses independently generated data and does not contain proprietary, confidential, or personally identifiable information.

The predictions produced by this project are intended for demonstration and educational purposes and should not be treated as production reliability guarantees.

---

## Author

**Rebecca Charles**

---

## Project

If you find this project useful or interesting, feel free to explore the repository and follow its future development.

**ReliQora-AI — Predict. Assess. Improve Reliability.**


