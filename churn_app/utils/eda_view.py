import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
def render_eda_view(df: pd.DataFrame):
    st.markdown("<h1 style='color: #770A7A; text-align: center;'>Exploratory Data Analysis</h1>", unsafe_allow_html=True)
    
    # Dual Donut Chart: Gender & Churn
    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])

    fig.add_trace(
        go.Pie(
            labels=['Male', 'Female'], 
            values=df['gender'].value_counts(), 
            name="Gender", 
            hole=0.4,
            marker_colors=['#2B5C8F', '#770A7A']
        ), 1, 1
    )
    
    fig.add_trace(
        go.Pie(
            labels=['No', 'Yes'], 
            values=df['Churn'].value_counts(), 
            name="Churn", 
            hole=0.4,
            marker_colors=['#2B5C8F', '#770A7A']
        ), 1, 2
    )

    fig.update_layout(
        title_text="Gender and Churn Distributions",
        annotations=[
            dict(text='Gender', x=0.18, y=0.5, font_size=16, showarrow=False),
            dict(text='Churn', x=0.82, y=0.5, font_size=16, showarrow=False)
        ]
    )

    st.plotly_chart(fig, use_container_width=True)
    # ---------------------------------------------------------

    # 2. Sunburst Chart: Churn Distribution w.r.t Gender
    f_yes = len(df[(df['gender'] == 'Female') & (df['Churn'] == 'Yes')])
    m_yes = len(df[(df['gender'] == 'Male') & (df['Churn'] == 'Yes')])
    f_no  = len(df[(df['gender'] == 'Female') & (df['Churn'] == 'No')])
    m_no  = len(df[(df['gender'] == 'Male') & (df['Churn'] == 'No')])

    labels = ["Churn: Yes", "Churn: No", "F_Yes", "M_Yes", "F_No", "M_No"]
    parents = ["", "", "Churn: Yes", "Churn: Yes", "Churn: No", "Churn: No"]
    values = [f_yes + m_yes, f_no + m_no, f_yes, m_yes, f_no, m_no]

    colors = ["royalblue", "firebrick", "deepskyblue", "skyblue", "tomato", "salmon"]

    fig2 = go.Figure(go.Sunburst(
        labels=labels,
        parents=parents,
        values=values,
        branchvalues="total",
        textinfo="label+percent parent",
        marker=dict(colors=colors)
    ))

    fig2.update_layout(
        title="Churn Distribution w.r.t Gender",
        template="plotly_white"
    )

    st.plotly_chart(fig2, use_container_width=True)
    # ---------------------------------------------------------
    # INTERACTIVE CATEGORICAL FEATURE INSPECTOR (AUTOMATED COLORS)
    # ---------------------------------------------------------
    st.markdown("<h2 style='color: #770A7A;'>Categorical Feature Inspector</h2>", unsafe_allow_html=True)

    cat_features = [
        "Contract", "PaymentMethod", "InternetService", "Dependents", 
        "Partner", "SeniorCitizen", "OnlineSecurity", "PaperlessBilling", 
        "TechSupport", "PhoneService"
    ]

    col_select, col_mode = st.columns([2, 1])

    with col_select:
        selected_feature = st.selectbox("Select Feature to Analyze:", cat_features)

    with col_mode:
        analysis_mode = st.radio(
            "Analysis View:", 
            ["Standalone Distribution", "Impact on Churn"],
            horizontal=True
        )

    # Render dynamic plot with automated color palette mapping
    if analysis_mode == "Standalone Distribution":
        if selected_feature == "PaymentMethod":
            fig = px.pie(
                df, 
                names=selected_feature, 
                hole=0.3, 
                title=f"<b>{selected_feature} Distribution</b>",
                color_discrete_sequence=px.colors.qualitative.Plotly  # Automated multi-category palette
            )
        else:
            fig = px.histogram(
                df, 
                x=selected_feature, 
                color=selected_feature,  # Automatically creates individual bars with unique colors
                title=f"<b>{selected_feature} Distribution</b>",
                color_discrete_sequence=px.colors.qualitative.Plotly  # Adapts to 2, 3, 4+ categories automatically
            )
    else:
        # Impact on Churn (Bivariate view)
        fig = px.histogram(
            df, 
            x=selected_feature, 
            color="Churn", 
            barmode="group", 
            title=f"<b>{selected_feature} vs. Churn Impact</b>",
            color_discrete_map={"Yes": "#770A7A", "No": "#2B5C8F"}  # Standardized Churn mapping
        )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        bargap=0.15,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Restrict container width using columns
    col1, col2 = st.columns([1, 1])

    # --- 1. Monthly Charges KDE ---
    with col1:
        fig, ax = plt.subplots(figsize=(6, 2.8), facecolor="none")
        ax.set_facecolor("none")

        sns.kdeplot(df[df["Churn"] == 'No']["MonthlyCharges"], color="#2B5C8F", fill=True, ax=ax, label="Not Churn")
        sns.kdeplot(df[df["Churn"] == 'Yes']["MonthlyCharges"], color="#770A7A", fill=True, ax=ax, label="Churn")

        ax.set_title('Distribution of Monthly Charges', fontweight='bold', color='#E0E0E0', fontsize=10, pad=10)
        ax.set_xlabel('Monthly Charges ($)', color='#E0E0E0', fontsize=8)
        ax.set_ylabel('Density', color='#E0E0E0', fontsize=8)
        ax.tick_params(colors='#E0E0E0', labelsize=8)

        legend = ax.legend(loc='upper right', facecolor='#1E1E1E', edgecolor='none', fontsize=7)
        for text in legend.get_texts():
            text.set_color("#E0E0E0")

        sns.despine()
        plt.tight_layout()
        st.pyplot(fig, transparent=True)

    # --- 2. Total Charges KDE ---
    with col2:
        fig2, ax2 = plt.subplots(figsize=(6, 2.8), facecolor="none")
        ax2.set_facecolor("none")

        sns.kdeplot(df[df["Churn"] == 'No']["TotalCharges"], color="#2B5C8F", fill=True, ax=ax2, label="Not Churn")
        sns.kdeplot(df[df["Churn"] == 'Yes']["TotalCharges"], color="#770A7A", fill=True, ax=ax2, label="Churn")

        ax2.set_title('Distribution of Total Charges', fontweight='bold', color='#E0E0E0', fontsize=10, pad=10)
        ax2.set_xlabel('Total Charges ($)', color='#E0E0E0', fontsize=8)
        ax2.set_ylabel('Density', color='#E0E0E0', fontsize=8)
        ax2.tick_params(colors='#E0E0E0', labelsize=8)

        legend2 = ax2.legend(loc='upper right', facecolor='#1E1E1E', edgecolor='none', fontsize=7)
        for text in legend2.get_texts():
            text.set_color("#E0E0E0")

        sns.despine()
        plt.tight_layout()
        st.pyplot(fig2, transparent=True)
        # Ensure numeric types
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # =========================================================
    # 1. TENURE VS CHURN BOX PLOT (Plotly)
    # =========================================================
    fig_box = px.box(
        df, 
        x='Churn', 
        y='tenure', 
        color='Churn',
        title='<b>Tenure vs Churn</b>',
        color_discrete_map={'Yes': '#770A7A', 'No': '#2B5C8F'}
    )

    fig_box.update_layout(
        xaxis_title='Churn',
        yaxis_title='Tenure (Months)',
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        height=400
    )

    st.plotly_chart(fig_box, use_container_width=True)

    # =========================================================
    # 2. NUMERIC FEATURE PAIRPLOT - KDE CONTOURS (Seaborn)
    # =========================================================
    st.markdown("<h3 style='color: #770A7A;'>Numerical Pairwise Distributions</h3>", unsafe_allow_html=True)

    # Select numeric features
    numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']

    # Generate KDE pairplot matching your app theme (#770A7A & #2B5C8F)
    g = sns.pairplot(
        df[numeric_cols].dropna(), 
        hue='Churn', 
        kind='kde', 
        corner=False,
        palette={'Yes': '#770A7A', 'No': '#2B5C8F'}
    )

    # Apply dark-mode transparency and text visibility
    g.fig.set_facecolor('none')
    for ax in g.axes.flat:
        if ax is not None:
            ax.set_facecolor('none')
            ax.xaxis.label.set_color('#E0E0E0')
            ax.yaxis.label.set_color('#E0E0E0')
            ax.tick_params(colors='#E0E0E0')
            for spine in ax.spines.values():
                spine.set_color('#E0E0E0')

    # Render in Streamlit with transparent background
    st.pyplot(g.fig, transparent=True)