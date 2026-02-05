# MLOps Labs Repository

Name: Sushritha Bharadwaj  
Course: MLOps  

This repository contains lab assignments for the MLOps course.

---

## Structure

- Lab1: Statistics utilities, testing, CI/CD
- Lab2: Airflow-based machine learning pipeline (customized)
- airflow_local: Local Airflow setup using Docker

---

## Lab2 Summary

Lab2 implements an automated ML pipeline using Apache Airflow.

Features:
- External dataset integration
- Data preprocessing with scaling
- KMeans clustering with elbow method
- Model and scaler persistence
- Consistent inference pipeline
- Docker-based Airflow deployment

---

## Run Lab2 (Local Test)

```bash
python -c "from Lab2.src.lab import load_data, data_preprocessing, build_save_model, load_model_elbow; a=load_data(); b=data_preprocessing(a); c=build_save_model(b,'model.sav'); print('Prediction:', load_model_elbow('model.sav', c))"
