import shap
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_resource
def get_cached_shap_explainer(_pipeline, bg_df):
    """
    1. Prétraite le dataset de fond (background dataset) avec le pipeline.
    2. Instancie et met en cache l'explainer sur le modèle final uniquement.
    """
    # Isoler les colonnes utiles
    feature_cols = [c for c in bg_df.columns if c not in ['customerID', 'Churn']]
    bg_sample = bg_df[feature_cols].sample(min(30, len(bg_df)), random_state=42)

    # Prétraiter le background sample via toutes les étapes du pipeline sauf la dernière
    X_bg_transformed = _pipeline[:-1].transform(bg_sample)
    
    # Récupérer le modèle final (ex: SVM)
    model = _pipeline[-1]

    # Fonction wrapper rapide travaillant directement sur la matrice numérique
    def predict_proba_transformed(x):
        return model.predict_proba(x)[:, 1]

    # Créer l'explainer optimisé
    explainer = shap.KernelExplainer(predict_proba_transformed, X_bg_transformed)
    return explainer


def plot_local_shap(pipeline, input_data, bg_df):
    """
    Calcule et affiche le graphique Waterfall SHAP de manière quasi-instantanée.
    """
    # 1. Charger l'explainer mis en cache
    explainer = get_cached_shap_explainer(pipeline, bg_df)

    # 2. Transformer uniquement l'entrée utilisateur
    feature_cols = [c for c in input_data.columns if c in bg_df.columns]
    input_df = input_data[feature_cols]
    
    X_input_transformed = pipeline[:-1].transform(input_df)

    # 3. Calculer les valeurs SHAP (ultra-rapide car pas de re-transformation)
    raw_shap_vals = explainer.shap_values(X_input_transformed, nsamples=100, l1_reg="auto")

    base_val = explainer.expected_value
    if isinstance(base_val, (list, np.ndarray)):
        base_val = base_val[0]

    shap_vals = np.array(raw_shap_vals[0] if isinstance(raw_shap_vals, list) else raw_shap_vals).flatten()

    # Noms des features après transformation (si le pipeline conserve les noms ou via get_feature_names_out)
    try:
        feature_names = pipeline[:-1].get_feature_names_out()
    except AttributeError:
        feature_names = [f"Feature {i}" for i in range(X_input_transformed.shape[1])]

    # 4. Construire l'objet Explanation
    explanation = shap.Explanation(
        values=shap_vals,
        base_values=base_val,
        data=X_input_transformed[0],
        feature_names=feature_names
    )

    # 5. Rendering Matplotlib optimisé pour le Dark Mode
    plt.close('all')
    fig, ax = plt.subplots(figsize=(8, 5.5))
    fig.patch.set_facecolor('#0e1626')
    ax.set_facecolor('#131d31')

    shap.plots.waterfall(explanation, max_display=10, show=False)

    current_ax = plt.gca()
    current_ax.set_facecolor('#131d31')

    for text in current_ax.texts:
        text.set_color('#ffffff')
    for spine in current_ax.spines.values():
        spine.set_color('#1e2c45')

    current_ax.tick_params(colors='#ffffff', labelsize=9)
    current_ax.xaxis.label.set_color('#ffffff')

    plt.tight_layout()
    return fig