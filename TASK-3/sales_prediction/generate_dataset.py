"""
generate_dataset.py
Generates a synthetic advertising dataset (TV, Radio, Newspaper spend -> Sales)
similar to the classic "Advertising.csv" dataset used in sales prediction tutorials.
Run this once to create data/Advertising.csv
"""

import numpy as np
import pandas as pd

np.random.seed(42)

n = 200

tv = np.random.uniform(0, 300, n)
radio = np.random.uniform(0, 50, n)
newspaper = np.random.uniform(0, 100, n)

# Sales depends mostly on TV and Radio, weakly on Newspaper, plus noise
sales = (
    7
    + 0.045 * tv
    + 0.19 * radio
    + 0.01 * newspaper
    + np.random.normal(0, 1.5, n)
)
sales = np.clip(sales, 1, None)

df = pd.DataFrame({
    "TV": tv.round(2),
    "Radio": radio.round(2),
    "Newspaper": newspaper.round(2),
    "Sales": sales.round(2),
})

df.to_csv("data/Advertising.csv", index_label="Index")
print("Saved data/Advertising.csv with", len(df), "rows")
