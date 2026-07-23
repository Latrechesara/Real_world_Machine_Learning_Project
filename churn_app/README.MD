# 📞 Telecom Churn Intelligence Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io) **[🚀 Launch Live Demo App](https://share.streamlit.io)**



An interactive Machine Learning dashboard built with **Streamlit**, **Scikit-Learn**, **SHAP**, and **Plotly** to analyze customer retention, perform EDA, and generate explainable churn predictions.

![App Banner](churn_app/assets/churn.png)

---

## 🌟 Features

* **Executive Summary**: High-level retention KPIs and dataset overview.
* **Exploratory Data Analysis**: Interactive Plotly charts for feature distributions and churn drivers.
* **Single-Customer Prediction**: Real-time scoring interface for individual customer profiles.
* **Explainable AI (XAI)**: Local SHAP force plots explaining prediction factors.

---

## 🏗️ Project Structure

```text
churn_app/
├── assets/
│   └── churn.png
├── notebooks/
│   ├── assets/
│   ├── 1-Exploratory_Data_Analysis.ipynb
│   ├── 2-Model_training_comparaison.ipynb
│   └── 3-Final_pipeline_fine_tuning.ipynb
├── utils/
│   ├── __init__.py
│   ├── eda_view.py
│   ├── explainability.py
│   ├── feature_engineering.py
│   ├── prediction_view.py
│   └── summary_view.py
├── app.py
├── champion_svm_pipeline.pkl
├── data.csv
└── requirements.txt

📓 Notebooks
The research pipeline spans three sequential notebooks covering exploratory data analysis, comparative
benchmarking across multiple ML models, and final hyperparameter fine-tuning with cross-validation
to export the champion pipeline.

🚀 Quick Start
1. Clone & Setup
git clone [https://github.com/latrechesara/real_world_machine_learning_project.git](https://github.com/latrechesara/real_world_machine_learning_project.git)
cd real_world_machine_learning_project
python -m venv venv

2. Activate Environment
Windows: venv\Scripts\activate

macOS/Linux: source venv/bin/activate

3. Install & Run
Bash
pip install -r churn_app/requirements.txt
streamlit run churn_app/app.py

🛠️ Tech Stack
UI: Streamlit

ML Pipeline: Scikit-Learn, Joblib

Explainability: SHAP

Data & Plots: Pandas, NumPy, Plotly
