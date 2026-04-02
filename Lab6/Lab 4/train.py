import os
from datetime import datetime

import joblib
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


VERSION_FILE_NAME = "model_version.txt"


def download_data():
    """Load the Wine dataset."""
    wine = load_wine()
    X = pd.DataFrame(wine.data, columns=wine.feature_names)
    y = pd.Series(wine.target, name="target")
    return X, y


def preprocess_data(X, y):
    """Split the dataset into training and testing sets."""
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    """Train a Random Forest classifier."""
    model = RandomForestClassifier(
        n_estimators=150,
        max_depth=6,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model


def get_model_version(version_file_name):
    """Read the current model version from a local file."""
    if os.path.exists(version_file_name):
        with open(version_file_name, "r") as file:
            content = file.read().strip()
            if content.isdigit():
                return int(content)
    return 0


def update_model_version(version_file_name, version):
    """Update the model version in a local file."""
    with open(version_file_name, "w") as file:
        file.write(str(version))


def save_model_locally(model, version):
    """Save the trained model locally in the models folder."""
    os.makedirs("models", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    model_path = f"models/model_v{version}_{timestamp}.joblib"
    joblib.dump(model, model_path)
    return model_path


def save_predictions(y_test, y_pred):
    """Save actual and predicted values to a CSV file."""
    os.makedirs("outputs", exist_ok=True)
    results = pd.DataFrame({
        "actual": y_test.reset_index(drop=True),
        "predicted": pd.Series(y_pred)
    })
    results_path = "outputs/predictions.csv"
    results.to_csv(results_path, index=False)
    return results_path


def main():
    # Get current version and increment it
    current_version = get_model_version(VERSION_FILE_NAME)
    new_version = current_version + 1

    # Load and preprocess data
    X, y = download_data()
    X_train, X_test, y_train, y_test = preprocess_data(X, y)

    # Train model
    model = train_model(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f"Model Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(report)

    # Save predictions
    predictions_path = save_predictions(y_test, y_pred)
    print(f"Predictions saved at: {predictions_path}")

    # Save model locally
    model_path = save_model_locally(model, new_version)
    print(f"Model saved locally at: {model_path}")

    # Update local version file
    update_model_version(VERSION_FILE_NAME, new_version)
    print(f"Model version updated to: {new_version}")


if __name__ == "__main__":
    main()