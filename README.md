# Decode Labs AI Internship

This repository contains all projects completed during my AI Internship at Decode Labs, showing progression from rule-based logic to supervised machine learning to vector-based recommendation systems.

## Projects

### 1. Rule-Based Chatbot
A Python chatbot that responds to user input using predefined rules and pattern matching — the foundation project introducing conversational logic before moving into machine learning.

📁 [`project-1-rule-based-chatbot/`](./project-1-rule-based-chatbot)

**Tech:** Python

---

### 2. Iris Flower Classification (KNN)
A K-Nearest Neighbors classifier that predicts iris flower species from numeric measurements. Includes proper train/test splitting, feature scaling with `StandardScaler` (fit on training data only, to avoid data leakage), and full evaluation using accuracy, confusion matrix, and F1-score.

**Result:** 100% accuracy on the test set, with zero misclassifications across all three species.

📁 [`project-2-iris-classifier/`](./project-2-iris-classifier)

**Tech:** Python, pandas, scikit-learn

---

### 3. Tech Stack Recommender
A skill-based job role recommender that takes a user's skills as input and recommends the top 3 best-matching job roles, using **TF-IDF vectorization** and **cosine similarity** — rather than simple keyword counting, which can create ties between roles that match the same number of skills.

TF-IDF weights rare, specific skills (like "MachineLearning") higher than common ones (like "Python"), allowing the system to distinguish between closely related roles based on skill specificity rather than raw match count.

📁 [`project-3-tech-stack-recommender/`](./project-3-tech-stack-recommender)

**Tech:** Python, pandas, scikit-learn

---

## Progression Summary

| Project | Concept Introduced | Key Skill |
|---|---|---|
| 1. Rule-Based Chatbot | Conditional logic, pattern matching | Python fundamentals |
| 2. Iris Classifier | Supervised learning | scikit-learn, model evaluation |
| 3. Tech Stack Recommender | Vector-based similarity | TF-IDF, cosine similarity |

## Author

Kinza — CS undergraduate, AI Engineering specialization
GitHub: [kinza-ai-tech](https://github.com/kinza-ai-tech)