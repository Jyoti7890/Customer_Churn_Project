import streamlit as st
import pandas as pd
import joblib
import os

# Get base directory (VERY IMPORTANT for deployment)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@st.cache_data
def load_data():
    """
    Load the bank churn dataset.
    """
    file_path = os.path.join(BASE_DIR, 'bank_churn.csv')
    
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"Error: {file_path} not found. Please ensure the dataset is in the correct directory.")
        return None


@st.cache_resource
def load_model():
    """
    Load the pre-trained churn prediction pipeline.
    """
    model_path = os.path.join(BASE_DIR, 'models', 'churn_prediction_model.pkl')
    
    try:
        model = joblib.load(model_path)
        return model
    except FileNotFoundError:
        st.error(f"Error: {model_path} not found. Please ensure the model is in the 'models/' directory.")
        return None