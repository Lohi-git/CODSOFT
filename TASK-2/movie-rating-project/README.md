# Sales Prediction Using Python 📈

Task 4 of the CodSoft Data Science Internship.

Predicting product Sales based on advertising spend across TV, Radio and Newspaper.

## Structure

```
sales-prediction-project/
├── data/
│   └── advertising.csv     <- add this yourself, see below
├── notebook/
│   └── sales_prediction.ipynb
├── requirements.txt
└── README.md
```

## Dataset

Using the Advertising dataset linked in the task PDF (TV / Radio / Newspaper spend vs Sales). Download it and place it at `data/advertising.csv`. Not committing the raw csv since it's not originally mine.

## How to run

```bash
pip install -r requirements.txt
jupyter notebook notebook/sales_prediction.ipynb
```

or run it headless from terminal:

```bash
jupyter nbconvert --to notebook --execute notebook/sales_prediction.ipynb --output sales_prediction_output.ipynb
```

### Windows troubleshooting

If `pip install` fails with an `OSError` about a long file path (usually pointing into a `jupyterlab/galata` folder), Windows' default 260-character path limit is the culprit. Two fixes:

**Fix 1 - enable long paths (one-time, needs a restart)**

Run in PowerShell as Administrator:
```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```
Restart your PC, then re-run `pip install -r requirements.txt`.

**Fix 2 - skip JupyterLab, use classic Notebook instead (faster, no restart)**
```bash
pip uninstall jupyterlab -y
pip install notebook
jupyter notebook notebook/sales_prediction.ipynb
```

If `jupyter` still isn't recognized as a command after installing, run it through Python directly instead:
```bash
python -m notebook notebook/sales_prediction.ipynb
```

## Approach

- Quick null check + dropped a leftover index column
- EDA: histograms per channel, scatter plots vs Sales, and a correlation heatmap
- Train/test split (80/20)
- Trained Linear Regression as a baseline, then Random Forest Regressor
- Compared both using RMSE and R²
- Checked actual vs predicted plot + RF feature importances to confirm which channel matters most

## Key finding

TV ad spend has by far the strongest relationship with Sales. Radio has a moderate effect. Newspaper barely moves the needle — both the correlation heatmap and the trained model's feature importance agree on this.

## Possible improvements

- Try interaction terms (e.g. TV × Radio) since channels might work better combined
- Hyperparameter tuning on the Random Forest
- Try Gradient Boosting for comparison

---
#codsoft #internship #datascience
