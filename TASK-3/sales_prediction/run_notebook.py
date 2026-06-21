# Suppress Warnings
import warnings
warnings.filterwarnings('ignore')

# Import the numpy and pandas package
import numpy as np
import pandas as pd

# Data Visualisation
import matplotlib.pyplot as plt 
import seaborn as sns

print("--- Step 1: Loading Data ---")
advertising = pd.DataFrame(pd.read_csv("data/Advertising.csv"))
print("Advertising head:\n", advertising.head())

print("\n--- Step 2: Data Inspection ---")
print("Advertising shape:", advertising.shape)

print("\nAdvertising info:")
advertising.info()

print("\nAdvertising describe:\n", advertising.describe())

print("\nNull values check (%):")
print(advertising.isnull().sum()*100/advertising.shape[0])

# Outlier Analysis
fig, axs = plt.subplots(3, figsize = (5,5))
plt1 = sns.boxplot(advertising['TV'], ax = axs[0])
plt2 = sns.boxplot(advertising['Newspaper'], ax = axs[1])
plt3 = sns.boxplot(advertising['Radio'], ax = axs[2])
plt.tight_layout()
plt.savefig("outputs/notebook_boxplot.png", dpi=150)
plt.close()

fig = plt.figure()
sns.boxplot(advertising['Sales'])
plt.savefig("outputs/notebook_sales_boxplot.png", dpi=150)
plt.close()

# Pairplot
sns.pairplot(advertising, x_vars=['TV', 'Newspaper', 'Radio'], y_vars='Sales', height=4, aspect=1, kind='scatter')
plt.savefig("outputs/notebook_pairplot.png", dpi=150)
plt.close()

# Heatmap
fig = plt.figure()
sns.heatmap(advertising.corr(), cmap="YlGnBu", annot = True)
plt.savefig("outputs/notebook_heatmap.png", dpi=150)
plt.close()

# Train/Test Split
X = advertising['TV']
y = advertising['Sales']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 100)

print("\n--- Step 3: Train/Test Split heads ---")
print("X_train head:\n", X_train.head())
print("y_train head:\n", y_train.head())

# Building Linear Model using Statsmodels
import statsmodels.api as sm

# Add a constant to get an intercept
X_train_sm = sm.add_constant(X_train)

# Fit the regression line using 'OLS'
lr = sm.OLS(y_train, X_train_sm).fit()

print("\n--- Step 4: Model parameters and summary ---")
print("lr.params:\n", lr.params)
print("\nOLS summary details:\n", lr.summary())

# Plot the regression line
fig = plt.figure()
plt.scatter(X_train, y_train)
plt.plot(X_train, lr.params['const'] + lr.params['TV']*X_train, 'r')
plt.savefig("outputs/notebook_fit.png", dpi=150)
plt.close()

# Residual Analysis
y_train_pred = lr.predict(X_train_sm)
res = (y_train - y_train_pred)

fig = plt.figure()
sns.histplot(res, bins = 15, kde=True)
fig.suptitle('Error Terms', fontsize = 15)                  # Plot heading 
plt.xlabel('y_train - y_train_pred', fontsize = 15)         # X-label
plt.savefig("outputs/notebook_residual_dist.png", dpi=150)
plt.close()

# Residual vs X_train plot
fig = plt.figure()
plt.scatter(X_train, res)
plt.savefig("outputs/notebook_residual_scatter.png", dpi=150)
plt.close()

# Predictions on Test set
X_test_sm = sm.add_constant(X_test)
y_pred = lr.predict(X_test_sm)

print("\n--- Step 5: Test Set Predictions ---")
print("y_pred head:\n", y_pred.head())

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r_squared = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.4f}")
print(f"R-squared: {r_squared:.4f}")

# Plot Test set regression line
fig = plt.figure()
plt.scatter(X_test, y_test)
plt.plot(X_test, lr.params['const'] + lr.params['TV'] * X_test, 'r')
plt.savefig("outputs/notebook_test_fit.png", dpi=150)
plt.close()

print("\nDone! Output files and plots successfully created and saved in outputs/ directory.")