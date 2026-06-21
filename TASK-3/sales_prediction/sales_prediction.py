"""
sales_prediction.py
--------------------
Internship Project: Sales Prediction Using Python

Goal: Predict product Sales based on advertising spend across
TV, Radio, and Newspaper channels using Linear Regression.

Steps:
1. Load & explore data
2. Visualize relationships (EDA)
3. Train/test split
4. Train Linear Regression model
5. Evaluate model (R2, MAE, RMSE)
6. Visualize predictions vs actual
7. Predict sales for new advertising budgets
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

sns.set_style("whitegrid")

# ---------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------
df = pd.read_csv("data/Advertising.csv", index_col="Index")
print("First 5 rows:\n", df.head())
print("\nDataset shape:", df.shape)
print("\nSummary statistics:\n", df.describe())
print("\nMissing values:\n", df.isnull().sum())

# ---------------------------------------------------------
# 2. Exploratory Data Analysis
# ---------------------------------------------------------
plt.figure(figsize=(6, 5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png", dpi=150)
plt.close()

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, col in zip(axes, ["TV", "Radio", "Newspaper"]):
    sns.scatterplot(data=df, x=col, y="Sales", ax=ax)
    ax.set_title(f"{col} vs Sales")
plt.tight_layout()
plt.savefig("outputs/feature_vs_sales.png", dpi=150)
plt.close()

# ---------------------------------------------------------
# 3. Train/Test Split
# ---------------------------------------------------------
X = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------------------------
# 4. Train Linear Regression Model
# ---------------------------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

print("\nModel Coefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"  {feature}: {coef:.4f}")
print(f"  Intercept: {model.intercept_:.4f}")

# ---------------------------------------------------------
# 5. Evaluate Model
# ---------------------------------------------------------
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\nModel Performance on Test Set:")
print(f"  R2 Score : {r2:.4f}")
print(f"  MAE      : {mae:.4f}")
print(f"  RMSE     : {rmse:.4f}")

# ---------------------------------------------------------
# 6. Visualize Predictions vs Actual
# ---------------------------------------------------------
plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color="steelblue")
plt.plot([y.min(), y.max()], [y.min(), y.max()], "r--", lw=2)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.tight_layout()
plt.savefig("outputs/actual_vs_predicted.png", dpi=150)
plt.close()

# ---------------------------------------------------------
# 7. Predict Sales for New Advertising Budgets
# ---------------------------------------------------------
new_budgets = pd.DataFrame({
    "TV": [150, 230, 50],
    "Radio": [25, 40, 5],
    "Newspaper": [10, 60, 5],
})
new_predictions = model.predict(new_budgets)

print("\nPredictions for new advertising budgets:")
for i, row in new_budgets.iterrows():
    print(
        f"  TV=${row.TV}, Radio=${row.Radio}, Newspaper=${row.Newspaper}"
        f"  ->  Predicted Sales = {new_predictions[i]:.2f} units"
    )

print("\nDone! Charts saved in the 'outputs/' folder.")
