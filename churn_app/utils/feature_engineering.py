import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class ChurnFeatureEngineer(BaseEstimator, TransformerMixin):
    def __init__(self, tenure_col="tenure", monthly_col="MonthlyCharges"):
        self.tenure_col = tenure_col
        self.monthly_col = monthly_col

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X_out = X.copy()
        X_out['Charges_to_Tenure_Ratio'] = X_out[self.monthly_col] / (X_out[self.tenure_col] + 1)
        return X_out

    # Safety alias in case your serialized model saved the typo method name 'tranform'
    def tranform(self, X):
        return self.transform(X)