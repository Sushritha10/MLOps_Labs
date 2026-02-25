# MLOps Labs Repository

**Name:** Sushritha Bharadwaj  
**Course:** MLOps  

This repository contains lab assignments and projects developed for the MLOps course, focusing on machine learning systems, automation, orchestration, and reproducible pipelines.

---

## Repository Structure

- **Lab1/** – Statistics utilities, testing, and CI/CD workflows  
- **Lab2/** – Automated ML pipeline with Airflow (data processing + clustering + modeling)  
- **Lab3/** – Advertising **Sales prediction** pipeline (regression, tuning, reproducibility)  
- **dags/** – Apache Airflow DAG definitions  
- **airflow_local/** – Local Airflow setup using Docker and Docker Compose  
- **logs/** – Airflow logs and pipeline artifacts (mounted from container)

---

## Lab1 Overview: Foundations & CI/CD

Lab1 focuses on building strong foundations for reliable machine learning systems.

### Features
- Statistical analysis utilities
- Data validation and testing
- Unit tests with PyTest
- Continuous Integration using GitHub Actions
- Code quality checks
- Reproducible experiment workflows

### Purpose
Establishes best practices for:
- Testing ML code
- Preventing data leakage
- Ensuring pipeline reliability
- Maintaining production-ready standards

---

## Lab2 Overview: Automated ML Pipeline with Airflow

Lab2 implements an automated machine learning pipeline using **Apache Airflow** and **Docker**.

### Features
- External dataset integration
- Data preprocessing with feature scaling
- KMeans clustering with elbow method
- Automatic selection of optimal k
- Model and scaler persistence
- Reusable inference pipeline
- Containerized Airflow environment

### Purpose
Demonstrates end-to-end MLOps workflows including:
- Pipeline orchestration
- Model training automation
- Versioned artifacts
- Reproducible execution
- Local containerized deployment

---

## Lab3 Overview: Advertising Sales Prediction (Regression)

Lab3 builds a clean, reproducible **regression** pipeline to predict **Sales** from advertising spend using the dataset with columns:

- `TV`, `Radio`, `Newspaper` → features  
- `Sales` → target

### What I changed / added (to ensure it’s not identical to the base repo)
- **Changed the task** to regression (Sales prediction) using the advertising spend dataset
- Implemented a full **scikit-learn Pipeline** to ensure consistent preprocessing + training:
  - `ColumnTransformer` + `StandardScaler` for numeric feature scaling
  - Model step using **Ridge Regression**
- Added **GridSearchCV** hyperparameter tuning:
  - tuned `alpha` for Ridge regression
  - cross-validated scoring using **R²**
- Added evaluation metrics for model quality:
  - **RMSE** (computed from MSE for compatibility)
  - **R² score**
- Saved the **entire pipeline artifact** (preprocessing + model together) so inference matches training exactly:
  - `model/sales_model.pkl`
- Added a standalone **prediction script** that loads the saved pipeline and produces predictions for a provided CSV file

### How to run Lab3
From the repository root:

```bash
cd Lab3
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/train.py
python src/predict.py data/advertising.csv