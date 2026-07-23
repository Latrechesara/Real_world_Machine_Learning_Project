import sys
import joblib
import pandas as pd
import streamlit as st

# 1. Import utility components & views from utils package
from utils import (
    ChurnFeatureEngineer, 
    plot_local_shap, 
    render_executive_summary, 
    render_eda_view
)

# 2. Register custom transformer class to __main__ for seamless joblib unpickling
sys.modules['__main__'].ChurnFeatureEngineer = ChurnFeatureEngineer

# 3. Streamlit Page Configuration
st.set_page_config(
    page_title="Telecom Churn Intelligence Platform",
    page_icon="📞",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 4. Resource Caching Loaders
@st.cache_resource
def load_pipeline():
    return joblib.load("champion_svm_pipeline.pkl")

@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    return df

# Load Assets
try:
    pipeline = load_pipeline()
    df = load_data()
except Exception as e:
    st.error(f"⚠️ Failed to load core app dependencies: {e}")
    st.stop()

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
st.sidebar.title("Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Go to",
    [
        "Executive Summary",
        "Data Analysis & EDA",
        "Single Customer Prediction"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Model Info**: Tuned SVM (RBF Kernel)\n\n**Threshold**: `0.459` | **ROC-AUC**: `0.84`")

# ---------------------------------------------------------
# Page Routing
# ---------------------------------------------------------

# View 1: Executive Summary
if page == "Executive Summary":
    render_executive_summary()

# View 2: Standalone EDA & Data Analysis
elif page == "Data Analysis & EDA":
    render_eda_view(df)

# View 3: Single Customer Risk Evaluator & SHAP Explainer
elif page == "Single Customer Prediction":
    st.title("🔮 Single Customer Churn Risk Evaluator")
    st.markdown("Enter customer demographic, contract, and billing metrics to evaluate real-time churn probability and local SHAP feature drivers.")

    st.write("---")
    
    with st.form("prediction_form"):
        st.subheader("Customer Demographics & Account Profile")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            gender = st.selectbox("Gender", options=["Male", "Female"])
            senior_citizen = st.selectbox("Senior Citizen", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
            partner = st.selectbox("Partner", options=["Yes", "No"])
            dependents = st.selectbox("Dependents", options=["Yes", "No"])
            tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=12)

        with col2:
            phone_service = st.selectbox("Phone Service", options=["Yes", "No"])
            multiple_lines = st.selectbox("Multiple Lines", options=["No phone service", "No", "Yes"])
            internet_service = st.selectbox("Internet Service", options=["DSL", "Fiber optic", "No"])
            online_security = st.selectbox("Online Security", options=["No", "Yes", "No internet service"])
            online_backup = st.selectbox("Online Backup", options=["No", "Yes", "No internet service"])
            device_protection = st.selectbox("Device Protection", options=["No", "Yes", "No internet service"])

        with col3:
            tech_support = st.selectbox("Tech Support", options=["No", "Yes", "No internet service"])
            streaming_tv = st.selectbox("Streaming TV", options=["No", "Yes", "No internet service"])
            streaming_movies = st.selectbox("Streaming Movies", options=["No", "Yes", "No internet service"])
            contract = st.selectbox("Contract Type", options=["Month-to-month", "One year", "Two year"])
            paperless_billing = st.selectbox("Paperless Billing", options=["Yes", "No"])
            payment_method = st.selectbox("Payment Method", options=[
                "Electronic check", "Mailed check", 
                "Bank transfer (automatic)", "Credit card (automatic)"
            ])
            monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=65.0)
            total_charges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=500.0)

        submit_btn = st.form_submit_button("Run Churn Prediction", use_container_width=True)

    if submit_btn:
        input_data = pd.DataFrame([{
            'gender': gender,
            'SeniorCitizen': senior_citizen,
            'Partner': partner,
            'Dependents': dependents,
            'tenure': tenure,
            'PhoneService': phone_service,
            'MultipleLines': multiple_lines,
            'InternetService': internet_service,
            'OnlineSecurity': online_security,
            'OnlineBackup': online_backup,
            'DeviceProtection': device_protection,
            'TechSupport': tech_support,
            'StreamingTV': streaming_tv,
            'StreamingMovies': streaming_movies,
            'Contract': contract,
            'PaperlessBilling': paperless_billing,
            'PaymentMethod': payment_method,
            'MonthlyCharges': monthly_charges,
            'TotalCharges': total_charges
        }])

        try:
            # Predict churn probability
            prob = pipeline.predict_proba(input_data)[0][1]

            st.write("---")
            st.subheader("🎯 Prediction Assessment")
            
            # Evaluate against optimized threshold 0.459
            if prob >= 0.459:
                st.error(f" **High Churn Risk Detected** (Predicted Probability: **{prob:.1%}**)")
                st.warning("Action Recommended: Trigger automated retention intervention discount.")
            else:
                st.success(f" **Low Churn Risk / Retained Profile** (Predicted Probability: **{prob:.1%}**)")

            st.write("---")
            st.subheader(" Local Prediction Explainability (SHAP Values)")
            with st.spinner("Calculating SHAP feature attributions..."):
                # Clean background dataset: safely remove metadata/target columns
                bg_df = df.drop(columns=['customerID', 'Churn'], errors='ignore')
                fig = plot_local_shap(pipeline, input_data, bg_df)
                st.pyplot(fig)
                
        except Exception as err:
            st.error(f"Inference Failure: {err}")