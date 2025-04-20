# 💳 Credit Card Fraud Detection - Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project explores patterns in credit card transactions to uncover behaviors that may indicate fraud. Using an anonymized dataset of European card transactions, we perform an in-depth exploratory data analysis (EDA) to understand what differentiates fraudulent transactions from normal ones.

---

## 📂 Dataset

- **Source**: [Kaggle – Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- **Size**: 284,807 transactions
- **Features**:
  - `Time`, `Amount`
  - 28 anonymized features (V1–V28) obtained via PCA
  - `Class` (Target): 0 = Normal, 1 = Fraud

---

## 🎯 Objective

- Understand the nature and distribution of fraud vs normal transactions
- Identify key features that signal fraud
- Visualize imbalances and patterns
- Prepare insights for future modeling

---

## 🔍 Exploratory Analysis Highlights

1. **Class Imbalance**  
   - Only **0.17%** of transactions are fraudulent  
   - Heavy class imbalance makes this a great case for anomaly detection

2. **Amount Analysis**  
   - Fraud transactions tend to have slightly higher average amounts  
   - Amount alone is not a strong indicator of fraud

3. **Time-Based Patterns**  
   - Fraud tends to occur in specific time windows  
   - May indicate bursts or planned attacks

4. **Feature Behavior**  
   - Features like `V4`, `V10`, `V11`, `V14`, and `V17` show **distinct patterns** in fraud cases  
   - Useful for future feature selection in machine learning

5. **Visual Insights**  
   - Boxplots and KDE plots reveal feature value differences between fraud and normal  
   - PCA scatter plots show clustering potential

---

## 📈 Visualizations Included

- Distribution plots (Amount, Time)
- Correlation matrix
- Boxplots of important features
- PCA-based 2D scatter plot
- Bar plots showing fraud distribution

---

## 🧠 Next Steps

- Feature selection and scaling
- Model building (Logistic Regression, Random Forest, XGBoost)
- Addressing class imbalance using SMOTE or undersampling
- Creating evaluation metrics (Precision, Recall, F1, AUC)

---

