import numpy as np
import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from imblearn.over_sampling import SMOTE

SEED = 77

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'creditcard.csv')
MODEL_DIR  = os.path.join(os.path.dirname(__file__), '..', 'models')
os.makedirs(MODEL_DIR, exist_ok=True)

print('loading data...')
df = pd.read_csv(DATA_PATH)
print(f'shape: {df.shape}')
print(f'fraud %: {df["Class"].mean()*100:.4f}%')

df = df.drop(columns=['Time'])
scaler = StandardScaler()
df['Amount'] = scaler.fit_transform(df[['Amount']])

X = df.drop(columns=['Class'])
y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED, stratify=y)

print('applying SMOTE...')
smote = SMOTE(random_state=SEED)
X_train_sm, y_train_sm = smote.fit_resample(X_train, y_train)
print(f'after SMOTE — train size: {X_train_sm.shape}')

print('training random forest...')
rf_model = RandomForestClassifier(n_estimators=100, random_state=SEED, n_jobs=-1)
rf_model.fit(X_train_sm, y_train_sm)

preds = rf_model.predict(X_test)
proba = rf_model.predict_proba(X_test)[:, 1]
print(classification_report(y_test, preds, target_names=['Legit', 'Fraud']))
print(f'ROC-AUC: {roc_auc_score(y_test, proba):.4f}')

joblib.dump(rf_model, os.path.join(MODEL_DIR, 'rf_model.pkl'))
joblib.dump(scaler,   os.path.join(MODEL_DIR, 'scaler.pkl'))
print('saved rf_model.pkl and scaler.pkl to /models/')
