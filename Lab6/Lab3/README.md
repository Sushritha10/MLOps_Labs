# Lab 3 — Advertising Sales Prediction (Modified)

This project predicts **Sales** from advertising spend using the dataset with columns:
`TV`, `Radio`, `Newspaper`, `Sales`.

## What I changed (so it’s not identical to the base lab)
- Switched to a **regression** task (Sales prediction)
- Built a full sklearn **Pipeline** (StandardScaler + model)
- Added **GridSearchCV** tuning (Ridge alpha)
- Saved the **entire pipeline** for consistent inference
- Reported **RMSE** and **R2**

## Structure