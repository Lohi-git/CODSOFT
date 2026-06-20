# Movie Rating Prediction 🎬

Task 2 of the CodSoft Data Science Internship.

Predicting a movie's rating based on stuff like genre, director, actors, duration and votes, using regression.

## What's in here

```
movie-rating-project/
├── data/
│   └── movies.csv              <- IMDb India movies dataset (add this yourself, see below)
├── notebook/
│   └── movie_rating_prediction.ipynb
├── requirements.txt
└── README.md
```

## Dataset

Using the IMDb Movies India dataset linked in the task PDF. Download it and drop it in `data/movies.csv` before running the notebook (not committing the raw csv to the repo since it's not mine to redistribute).

## How to run

```bash
pip install -r requirements.txt
jupyter notebook notebook/movie_rating_prediction.ipynb
```

## Approach (quick summary)

- Cleaned up Year/Duration/Votes columns (had junk like brackets, "min" text, commas in numbers)
- Dropped rows with no Rating since that's the target
- Genre column got split + manually one-hot encoded (movies can have multiple genres in one cell)
- Director and Actor columns target-encoded (mapped to avg rating, since one-hot would've made way too many columns)
- Trained Linear Regression as baseline, then Random Forest
- Evaluated using RMSE + R², checked residual plot to see if predictions made sense

## Results

Random Forest came out ahead of plain linear regression. Full numbers + plots are in the notebook output cells once you run it.

## Notes / things I'd improve later

- Target encoding here is done directly on the full data which leaks a bit of target info into the features — a cleaner version would use K-fold encoding
- Didn't do any hyperparameter tuning, just used reasonable defaults
- Could try XGBoost/LightGBM for a likely bump in performance

---
Built as part of #codsoft #internship #datascience
