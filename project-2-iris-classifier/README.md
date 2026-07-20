# Data Classification Using AI

A supervised learning project that classifies iris flowers into one of three species (setosa, versicolor, virginica) based on four numeric measurements, built as Project 2 for the AI Internship track at Decode Labs.

## What It Does

Uses the classic Iris dataset (150 samples) to train a K-Nearest Neighbors (KNN) classifier. The model learns from labeled flower measurements and predicts the species of unseen flowers with high accuracy.

## Pipeline

1. **Load Data** — Iris dataset from scikit-learn (4 features, 3 species)
2. **Train/Test Split** — 80% training, 20% testing (never seen by the model during training)
3. **Feature Scaling** — StandardScaler normalizes all features to a common scale
4. **Model Training** — K-Nearest Neighbors (k=5) learns patterns from training data
5. **Evaluation** — Accuracy, confusion matrix, and classification report (precision, recall, F1-score)

## Why Scaling Matters

Features are scaled using `fit_transform()` on training data only, then applied to test data with `transform()` — this prevents data leakage and ensures test data is treated as genuinely unseen information.

## Results

- **Accuracy:** 100% on test set
- **Confusion Matrix:** Zero misclassifications across all 3 species
- **F1-Score:** 1.00 for all classes

## Tech Used

- Python 3.12
- scikit-learn
- NumPy

## How to Run

```bash
pip install -r requirements.txt
python classifier.py
```

## What's Next

Future improvements could include testing different values of k, comparing KNN against other algorithms (e.g., logistic regression, decision trees), or applying this pipeline to a more complex, imbalanced dataset.