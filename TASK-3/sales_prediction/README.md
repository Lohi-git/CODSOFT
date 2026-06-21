# 📈 Sales Prediction Using Python

**Internship Project — Data Science / Machine Learning**

This project predicts product **Sales** based on advertising budgets spent on **TV, Radio, and Newspaper** using a **Linear Regression** model built in Python.

---

## 🎯 Objective

Businesses spend money advertising on different platforms. This project analyzes how advertising spend impacts sales and builds a machine learning model that can **predict future sales** based on planned ad budgets — helping with smarter marketing decisions.

---

## 🗂️ Project Structure

```
sales_prediction/
│
├── data/
│   └── Advertising.csv          # Dataset (TV, Radio, Newspaper, Sales)
├── outputs/
│   ├── correlation_heatmap.png
│   ├── feature_vs_sales.png
│   └── actual_vs_predicted.png
├── generate_dataset.py          # Script to (re)generate the dataset
├── sales_prediction.py          # Main project script (EDA + ML model)
├── requirements.txt
└── README.md
```

---

## 🧠 Approach

1. **Data Loading & Exploration** — inspect shape, stats, missing values
2. **EDA (Exploratory Data Analysis)** — correlation heatmap, scatter plots of each feature vs Sales
3. **Train/Test Split** — 80/20 split
4. **Model Training** — Linear Regression (`scikit-learn`)
5. **Evaluation** — R² Score, MAE, RMSE
6. **Visualization** — Actual vs Predicted sales plot
7. **Prediction** — forecast sales for new advertising budgets

---

## 📊 Dataset

The dataset (`data/Advertising.csv`) contains 200 records with:

| Column    | Description                          |
|-----------|---------------------------------------|
| TV        | Advertising budget spent on TV ($)    |
| Radio     | Advertising budget spent on Radio ($) |
| Newspaper | Advertising budget on Newspaper ($)   |
| Sales     | Units of product sold                 |

> Note: `generate_dataset.py` creates a synthetic dataset modeled after the classic "Advertising" dataset commonly used in sales-prediction tutorials. You can replace `data/Advertising.csv` with your own real dataset using the same column names.

---

## ⚙️ How to Run

1. Clone this repository
   ```bash
   git clone https://github.com/<your-username>/sales-prediction.git
   cd sales-prediction
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Regenerate the dataset
   ```bash
   python generate_dataset.py
   ```

4. Run the main script
   ```bash
   python sales_prediction.py
   ```

Charts will be saved in the `outputs/` folder, and model performance metrics will print to the console.

---

## 📈 Results

| Metric | Score |
|--------|-------|
| R² Score | ~0.93 |
| MAE | ~1.06 |
| RMSE | ~1.25 |

**Key Insight:** Radio and TV advertising have the strongest positive impact on sales, while Newspaper spend has a much weaker effect — suggesting marketing budget could be optimized by shifting more spend toward TV and Radio.

---

## 🛠️ Tech Stack

- Python 3
- pandas, numpy
- matplotlib, seaborn
- scikit-learn

---

## 🚀 Future Improvements

- Try other models (Random Forest, XGBoost) and compare performance
- Add cross-validation and hyperparameter tuning
- Build a simple Streamlit dashboard for interactive sales prediction
- Use a real-world advertising/sales dataset

---

## 👤 Author

Created as part of an internship project on Data Science / Machine Learning with Python.
