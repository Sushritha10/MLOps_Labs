# Lab 4 – Machine Learning Model Training and Local Model Versioning

## Overview
This lab implements a simple Machine Learning pipeline that trains a classification model, evaluates its performance, and manages model artifacts using local versioning.

The pipeline loads a dataset, preprocesses the data, trains a Random Forest classifier, evaluates the model using multiple metrics, and stores the trained model locally with automatic version tracking.

This implementation modifies the original lab template to demonstrate independent experimentation and improved project structure.

---

## Objectives

The goals of this lab are:

- Build a reproducible machine learning training pipeline
- Train and evaluate a classification model
- Save trained models as versioned artifacts
- Track model versions locally
- Export predictions for analysis
- Demonstrate a simplified MLOps workflow

---

## Modifications from the Original Lab

Several changes were made to ensure the lab is not identical to the original repository.

### 1. Dataset Change
The original lab used the **Iris dataset**.

This implementation uses the **Wine dataset** from Scikit-learn.

Reason:
- Demonstrates flexibility in data pipelines
- Shows independent dataset experimentation

---

### 2. Model Parameter Changes
The RandomForest model configuration was modified.

```python
RandomForestClassifier(
    n_estimators=150,
    max_depth=6,
    random_state=42
)
```

These changes demonstrate model tuning and experimentation.

---

### 3. Extended Model Evaluation
In addition to accuracy, the script prints a full **classification report** including:

- Precision
- Recall
- F1-score
- Support

This provides a more comprehensive view of model performance.

---

### 4. Prediction Export
Predictions are saved to a CSV file for further analysis.

Output file:

```
outputs/predictions.csv
```

The file contains:

| actual | predicted |

---

### 5. Local Model Artifact Storage
Instead of using cloud storage, the trained model is saved locally in the `models` folder.

Example model artifact:

```
models/model_v2_20260313170849.joblib
```

The filename includes:
- model version
- timestamp

---

### 6. Local Model Version Tracking
A version tracking system is implemented using a text file.

```
model_version.txt
```

Each time the training pipeline runs:

1. The current model version is read
2. The version number is incremented
3. The trained model is saved with the new version
4. The version file is updated

Example:

```
model_version.txt
2
```

---

## Project Structure

```
Lab 4
│
├── train.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   └── model_v2_20260313170849.joblib
│
├── outputs/
│   └── predictions.csv
│
└── model_version.txt
```

### File Descriptions

| File | Description |
|-----|-------------|
| train.py | Main script for data loading, training, evaluation, and artifact storage |
| requirements.txt | Python dependencies |
| README.md | Documentation for this lab |
| .gitignore | Prevents unnecessary files from being committed |
| models/ | Stores trained model artifacts |
| outputs/ | Stores prediction outputs |
| model_version.txt | Stores current model version |

---

## Installation

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies used:

- pandas
- scikit-learn
- joblib

---

## Running the Training Pipeline

Run the script:

```bash
python train.py
```

Example output:

```
Model Accuracy: 1.0000

Classification Report:
precision recall f1-score support

Predictions saved at: outputs/predictions.csv
Model saved locally at: models/model_v2_20260313170849.joblib
Model version updated to: 2
```

---

## Outputs Generated

After running the script, the following artifacts are created:

```
outputs/predictions.csv
models/model_vX_timestamp.joblib
model_version.txt
```

These files represent:

- evaluation results
- trained model artifacts
- version tracking metadata

---

## Key Concepts Demonstrated

This lab demonstrates several MLOps concepts:

- Reproducible machine learning pipelines
- Model artifact storage
- Model version tracking
- Evaluation metrics
- Prediction export
- Structured ML project organization

---

## Conclusion

This lab implements a simple end-to-end machine learning workflow including data loading, preprocessing, model training, evaluation, artifact storage, and version management.

The modifications ensure that the implementation differs from the original repository while still demonstrating core MLOps principles.