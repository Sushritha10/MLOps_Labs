import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from kneed import KneeLocator
import pickle
import os
import base64


def load_data():
    """
    Loads data from CSV and returns base64-encoded pickled DataFrame (JSON-safe).
    """
    path = os.path.join(os.path.dirname(__file__), "..", "data", "file.csv")
    df = pd.read_csv(path)

    serialized = pickle.dumps(df)
    return base64.b64encode(serialized).decode("ascii")


def data_preprocessing(data_b64: str):
    """
    Decodes input df, selects features, scales them, and returns:
      - scaled X (base64 pickled)
      - scaler (base64 pickled)
      - features list (JSON-safe)
    """
    data_bytes = base64.b64decode(data_b64)
    df = pickle.loads(data_bytes)

    df = df.dropna()

    features = ["Rank", "Population"]
    missing = [c for c in features if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}. Available: {df.columns.tolist()}")

    X = df[features].copy()

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    X_b64 = base64.b64encode(pickle.dumps(X_scaled)).decode("ascii")
    scaler_b64 = base64.b64encode(pickle.dumps(scaler)).decode("ascii")

    return {
        "X": X_b64,
        "scaler": scaler_b64,
        "features": features,
    }


def build_save_model(prep_artifact: dict, filename: str):
    """
    Runs SSE for k=1..14, chooses elbow k, trains final KMeans at best_k,
    saves the model to Lab2/model/<filename>, returns training artifact.
    """
    X_b64 = prep_artifact["X"]
    scaler_b64 = prep_artifact["scaler"]
    features = prep_artifact["features"]

    X = pickle.loads(base64.b64decode(X_b64))

    kmeans_kwargs = {
        "init": "k-means++",
        "n_init": 10,
        "max_iter": 300,
        "random_state": 42,
    }

    sse = []
    k_range = range(1, 15)
    for k in k_range:
        model = KMeans(n_clusters=k, **kmeans_kwargs)
        model.fit(X)
        sse.append(model.inertia_)

    kl = KneeLocator(list(k_range), sse, curve="convex", direction="decreasing")
    best_k = int(kl.elbow) if kl.elbow else 3

    final_model = KMeans(n_clusters=best_k, **kmeans_kwargs)
    final_model.fit(X)

    output_path = os.path.join(os.path.dirname(__file__), "..", "model", filename)
    with open(output_path, "wb") as f:
        pickle.dump(final_model, f)

    return {
        "sse": sse,
        "best_k": best_k,
        "scaler": scaler_b64,
        "features": features,
    }


def load_model_elbow(filename: str, train_artifact: dict):
    """
    Loads the saved model, uses scaler + features from train_artifact,
    predicts a cluster label for the first row in test.csv and returns int.
    """
    model_path = os.path.join(os.path.dirname(__file__), "..", "model", filename)
    model = pickle.load(open(model_path, "rb"))

    scaler = pickle.loads(base64.b64decode(train_artifact["scaler"]))
    features = train_artifact["features"]

    print("Chosen k:", train_artifact["best_k"])

    test_path = os.path.join(os.path.dirname(__file__), "..", "data", "test.csv")
    df_test = pd.read_csv(test_path)

    missing = [c for c in features if c not in df_test.columns]
    if missing:
        raise ValueError(f"Test data missing columns: {missing}. Available: {df_test.columns.tolist()}")

    X_test = df_test[features].copy()
    X_test_scaled = scaler.transform(X_test)

    pred = model.predict(X_test_scaled)[0]
    return int(pred)