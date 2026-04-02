from flask import Flask, request, render_template, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

CLASS_NAMES = ["Class 0 (Cultivar 1)", "Class 1 (Cultivar 2)", "Class 2 (Cultivar 3)"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [float(request.form[f"feature_{i}"]) for i in range(13)]
        prediction = model.predict([features])[0]
        result = CLASS_NAMES[prediction]
        return render_template("index.html", prediction=result)
    except Exception as e:
        return render_template("index.html", prediction=f"Error: {str(e)}")

@app.route("/health")
def health():
    return jsonify({"status": "ok", "model": "GradientBoostingClassifier", "dataset": "Wine"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
