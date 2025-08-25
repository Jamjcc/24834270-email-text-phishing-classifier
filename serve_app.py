# html.py
from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path
import threading, webbrowser, time

# Optional: load model artefacts
import joblib

BASE_DIR = Path(__file__).resolve().parent

# Serve files from the project folder itself (so relative assets work)
app = Flask(__name__, static_folder=str(BASE_DIR), static_url_path="")

# ---- Load your trained artefacts (adjust filenames if different) ----
try:
    VECT = joblib.load(BASE_DIR / "tfidf_vectorizer.pkl")        # e.g., your TF-IDF
    MODEL = joblib.load(BASE_DIR / "svm_phishing_model.pkl")     # e.g., your SVM
    MODEL_READY = True
    print("[OK] Model and vectorizer loaded.")
except Exception as e:
    MODEL_READY = False
    print(f"[WARN] Model not loaded: {e}\n"
          f"      Place tfidf_vectorizer.pkl and svm_phishing_model.pkl next to html.py.")

# ---- Routes ----
@app.get("/")
def index():
    # Serves ./app.html
    return send_from_directory(BASE_DIR, "app.html")

@app.post("/predict")
def predict():
    if not MODEL_READY:
        return jsonify({"error": "Model not loaded on server"}), 500
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    X = VECT.transform([text])
    pred = int(MODEL.predict(X)[0])
    proba = None
    if hasattr(MODEL, "predict_proba"):
        proba = float(MODEL.predict_proba(X)[0, 1])
    return jsonify({"prediction": pred, "probability": proba})

def open_browser():
    time.sleep(1)
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Thread(target=open_browser, daemon=True).start()
    app.run(host="127.0.0.1", port=5000, debug=False)
