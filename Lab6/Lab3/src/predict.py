import os
import sys
import pandas as pd
import joblib


def main():
    model_path = os.environ.get("MODEL_PATH", os.path.join("model", "sales_model.pkl"))
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at: {model_path}. Run training first.")

    if len(sys.argv) < 2:
        print("Usage: python src/predict.py <path_to_csv>")
        print("Example: python src/predict.py data/advertising.csv")
        sys.exit(1)

    csv_path = sys.argv[1]
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()

    # Use features only
    X = df[["TV", "Radio", "Newspaper"]]

    model = joblib.load(model_path)
    preds = model.predict(X)

    print("\n===== Lab3 Predictions (Sales) =====")
    print("Rows predicted:", len(preds))
    print("First 10 predicted sales:", [round(x, 3) for x in preds[:10]])


if __name__ == "__main__":
    main()