# MLOps Labs Repository

**Name:** Sushritha Bharadwaj  
**Course:** MLOps  

This repository contains lab assignments and projects developed for the MLOps course, focusing on machine learning systems, automation, and deployment.

---

## Repository Structure

- **Lab1/** – Statistics utilities, testing, and CI/CD workflows  
- **Lab2/** – Machine learning pipeline (data processing, clustering, modeling)  
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

## Running Lab2 with Airflow (Recommended)

### Prerequisites
- Docker Desktop
- Docker Compose v2

### Start Airflow

From the project root:

```bash
cd airflow_local
docker compose -f docker-compose.yaml up --build