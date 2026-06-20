# Credit Card Fraud Detection
### CodSoft Data Science Internship — Task 5

A complete end-to-end machine learning project to detect fraudulent credit card transactions using Random Forest with SMOTE for class imbalance handling.

---

## Project Structure

```
credit-card-fraud-detection/
│
├── backend/
│   ├── app.py              # Flask REST API
│   ├── train.py            # Model training script
│   └── requirements.txt    # Python dependencies
│
├── frontend/
│   └── index.html          # Web UI (no frameworks)
│
├── notebook/
│   └── credit_card_fraud_detection.ipynb   # Full EDA + modelling notebook
│
├── models/                 # Saved model files (generated after training)
│   ├── rf_model.pkl
│   └── scaler.pkl
│
└── README.md
```

---

## Dataset

Download `creditcard.csv` from Kaggle:  
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

Place it in the **root** of the project folder.

---

## Setup & Run

### 1. Install dependencies
```bash
pip install -r backend/requirements.txt
```

### 2. Train the model
```bash
python backend/train.py
```

### 3. Start the Flask API
```bash
python backend/app.py
```

### 4. Open the frontend
Open `frontend/index.html` in your browser.

---

## Models Used
- Logistic Regression (baseline)
- Random Forest (final model)

## Techniques
- SMOTE for class imbalance
- StandardScaler for feature scaling
- Confusion Matrix, ROC-AUC, Precision-Recall evaluation

---

## Results

| Model | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|
| Logistic Regression | ~0.87 | ~0.62 | ~0.72 | ~0.97 |
| Random Forest | ~0.95 | ~0.82 | ~0.88 | ~0.98 |

---

**Dataset:** Kaggle Credit Card Fraud Detection  
**Internship:** CodSoft Data Science
