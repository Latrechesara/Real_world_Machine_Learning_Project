# 📞 Telecom Churn Intelligence Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://churnapp-clohhlrh9yqntg3nqwnkv4.streamlit.app/)
**[🚀 Launch Live Demo App](https://churnapp-clohhlrh9yqntg3nqwnkv4.streamlit.app/)**

An interactive Machine Learning dashboard built with **Streamlit**, **Scikit-Learn**, **SHAP**, and **Plotly** to analyze customer retention, perform EDA, and generate explainable churn predictions.



An interactive Machine Learning dashboard built with **Streamlit**, **Scikit-Learn**, **SHAP**, and **Plotly** to analyze customer retention, perform EDA, and generate explainable churn predictions.


---

## 🌟 Features

* **Executive Summary**: High-level retention KPIs and dataset overview.
* **Exploratory Data Analysis**: Interactive Plotly charts for feature distributions and churn drivers.
* **Single-Customer Prediction**: Real-time scoring interface for individual customer profiles.
* **Explainable AI (XAI)**: Local SHAP force plots explaining prediction factors.

---


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
