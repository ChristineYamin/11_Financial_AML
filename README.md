# 🛡️ FinGuard AML Intelligence

### Project 11 | 23 Projects at 23 Portfolio

An enterprise-grade, real-time transaction monitoring application designed to detect financial anomaly patterns and potential money laundering activities. This system is optimized to counter severe class imbalances using state-of-the-art tree boosting architectures and targeted financial discrepancy feature engineering.

---

## 💡 System Architecture & Core Logic

In real-world Anti-Money Laundering (AML) pipelines, standard machine learning models struggle due to severe class imbalance (often fewer than 0.1% of transactions are fraudulent). 

FinGuard resolves this by implementing a custom **Mathematical Discrepancy Filter** within the feature layer. By analyzing the synthetic behavior profiles in the banking simulator, the pipeline explicitly exposes systematic transaction vulnerabilities where balances are artificially drained or mismatched:

$$\text{errorBalanceOrig} = \text{newbalanceOrig} + \text{amount} - \text{oldbalanceOrg}$$

Tree-based classifiers successfully capture these perfect logical splits, delivering high-performance recall thresholds required for institutional financial risk mitigation.

---

## 📊 Core Performance Metrics

* **Fraud Recall:** 100% (Zero missed financial anomalies on the validation split)
* **Precision:** 86% (Optimized to keep false-alarm friction low for legitimate clients)
* **Primary Risk Driver:** `errorBalanceOrig` (Accounting for 76% of overall model feature importance)

---

## ⚙️ Built With

* **Core Engine:** Python, XGBoost, Scikit-Learn
* **Serialization:** Joblib
* **Interface:** Streamlit (Custom Korean Minimalist Aesthetic)

---

## 🚀 Local Installation & Execution

To clone the repository and execute the dashboard locally on your machine, follow these steps:

1. Clone the project files:
   ```bash
   git clone [https://github.com/yourusername/11_financial_aml.git](https://github.com/yourusername/11_financial_aml.git)
   cd 11_financial_aml