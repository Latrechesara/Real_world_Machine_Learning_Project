import streamlit as st

def render_executive_summary():
    # Inject Custom CSS for dark-theme card components with elevated shadows
    st.markdown("""
        <style>
        .metric-card {
            background-color: #121216;
            border: 1px solid #2D2D38;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
            margin-bottom: 10px;
        }
        .metric-label {
            color: #A0A0B0;
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 6px;
        }
        .metric-value {
            color: #FFFFFF;
            font-size: 1.8rem;
            font-weight: 700;
            margin: 0;
        }
        .info-card {
            background-color: #121216;
            border: 1px solid #2D2D38;
            border-radius: 12px;
            padding: 24px;
            height: 100%;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
            margin-top: 10px;
        }
        .card-header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 16px;
        }
        .card-title {
            color: #FFFFFF;
            font-size: 1.25rem;
            font-weight: 600;
            margin: 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- 1. TITLE ---
    st.markdown("<h1 style='text-align: center;'>Telecom Customer Churn Intelligence System</h1>", unsafe_allow_html=True)    
    # --- 2. IMAGE DIRECTLY UNDER TITLE ---
    # Centered image layout using columns
    img_col1, img_col2, img_col3 = st.columns([1, 2, 1])
    with img_col2:
        st.image("assets/churn.png", use_container_width=True)

    st.markdown("<div style='margin: 15px 0;'></div>", unsafe_allow_html=True)

    # --- 3. BUSINESS PROBLEM & STRATEGY ---
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#770A7A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
        <h3 style="margin: 0; color: #FFFFFF; font-size: 1.35rem; font-weight: 600;">Business Problem & ML Strategy</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Customer acquisition costs **5× to 25× more** than retaining existing subscribers in the telecommunications industry. 
    This platform combines exploratory customer analytics with machine learning to identify churn risk early and enable proactive retention interventions.
    """)

    st.markdown("<div style='margin: 25px 0;'></div>", unsafe_allow_html=True)

    # --- 4. EXECUTIVE METRIC CARDS WITH SHADOWS ---
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="metric-card"><div class="metric-label">Champion Model</div><div class="metric-value" style="color: #4A90E2;">Tuned SVM</div></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-card"><div class="metric-label">ROC-AUC Score</div><div class="metric-value">0.84</div></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-card"><div class="metric-label">Decision Threshold</div><div class="metric-value" style="color: #770A7A;">0.459</div></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="metric-card"><div class="metric-label">Overall Accuracy</div><div class="metric-value">81%</div></div>', unsafe_allow_html=True)

    st.markdown("<div style='margin: 15px 0;'></div>", unsafe_allow_html=True)

    # --- 5. TECHNICAL DETAILS CARDS WITH LUCIDE ICONS ---
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.markdown("""
        <div class="info-card">
            <div class="card-header">
                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#2B5C8F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.38a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/></svg>
                <h4 class="card-title">Methodology & Pipeline</h4>
            </div>
            <ul>
                <li><b>Feature Engineering</b>: Ratio creation (<code>Charges_to_Tenure_Ratio</code>) handled inside custom scikit-learn pipeline.</li>
                <li style="margin-top: 8px;"><b>Cross-Validation</b>: 5-fold stratified cross-validation across multiple candidate models.</li>
                <li style="margin-top: 8px;"><b>Hyperparameter Tuning</b>: Optimal SVM parameters (<code>C=1.0</code>, <code>gamma=0.01</code>, RBF kernel).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.markdown("""
        <div class="info-card">
            <div class="card-header">
                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#770A7A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
                <h4 class="card-title">Calibration & Interpretability</h4>
            </div>
            <ul>
                <li><b>Decision Boundary</b>: Tuned cutoff at <code style="color:#770A7A; font-weight:bold;">0.459</code> balancing Precision (0.63) and Recall (0.65).</li>
                <li style="margin-top: 8px;"><b>PR-AUC Metric</b>: Achieved <b>0.63 PR-AUC</b> under class-imbalanced constraints.</li>
                <li style="margin-top: 8px;"><b>Explainable AI</b>: Real-time SHAP attribution for local customer predictions.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)