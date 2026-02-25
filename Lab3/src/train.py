import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score


def load_data(csv_path: str) -> pd.DataFrame:
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Could not find dataset at: {csv_path}")
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()
    return df


def main():
    csv_path = os.environ.get("CSV_PATH", os.path.join("data", "advertising.csv"))
    df = load_data(csv_path)

    # Expecting columns: TV, Radio, Newspaper, Sales
    required = {"TV", "Radio", "Newspaper", "Sales"}
    if not required.issubset(set(df.columns)):
        raise ValueError(
            f"Dataset columns are {list(df.columns)} but expected at least {sorted(required)}"
        )

    X = df[["TV", "Radio", "Newspaper"]]
    y = df["Sales"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    numeric_cols = X.columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[("num", StandardScaler(), numeric_cols)],
        remainder="drop",
    )

    model = Ridge()

    pipe = Pipeline(steps=[
        ("preprocess", preprocessor),
        ("model", model),
    ])

    param_grid = {
        "model__alpha": [0.01, 0.1, 1.0, 10.0, 100.0],
    }

    grid = GridSearchCV(
        estimator=pipe,
        param_grid=param_grid,
        scoring="r2",
        cv=5,
        n_jobs=-1
    )

    grid.fit(X_train, y_train)
    best_model = grid.best_estimator_

    preds = best_model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    rmse = mse ** 0.5
    r2 = r2_score(y_test, preds)

    print("\n===== Lab3 Training Results (Regression) =====")
    print("Best params:", grid.best_params_)
    print("RMSE:", round(rmse, 4))
    print("R2:", round(r2, 4))

    os.makedirs("model", exist_ok=True)
    out_path = os.path.join("model", "sales_model.pkl")
    joblib.dump(best_model, out_path)
    print(f"Saved full pipeline to: {out_path}")


if __name__ == "__main__":
    main()