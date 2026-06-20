from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import joblib
import os

app = Flask(__name__)
CORS(app)

# loading saved model and scaler
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'rf_model.pkl')
SCALER_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'scaler.pkl')

model = None
scaler = None

def load_artifacts():
    global model, scaler
    if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        print('model and scaler loaded')
    else:
        print('model files not found — run train.py first')

load_artifacts()


@app.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'fraud detection api is running'})


@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return jsonify({'error': 'model not loaded — run train.py first'}), 503

    data = request.get_json()
    if not data or 'features' not in data:
        return jsonify({'error': 'missing features in request body'}), 400

    try:
        features = np.array(data['features']).reshape(1, -1)

        # expecting 29 features: V1-V28 + Amount (Time dropped)
        if features.shape[1] != 29:
            return jsonify({'error': f'expected 29 features, got {features.shape[1]}'}), 400

        # scale the Amount (last column)
        features[:, -1] = scaler.transform(features[:, -1].reshape(-1, 1)).flatten()

        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]

        return jsonify({
            'prediction': int(prediction),
            'label': 'FRAUD' if prediction == 1 else 'LEGIT',
            'fraud_probability': round(float(probability), 4),
            'confidence': round(float(max(model.predict_proba(features)[0])) * 100, 2)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'ok',
        'model_loaded': model is not None,
        'scaler_loaded': scaler is not None
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
