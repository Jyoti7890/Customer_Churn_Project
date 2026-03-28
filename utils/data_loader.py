import streamlit as st
import pandas as pd
import joblib
import os
from io import StringIO

# Go one level up from utils folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _resolve_git_conflicts(lines):
    """
    Resolve plain-text Git conflict blocks by keeping the current branch
    section (`HEAD`) and discarding the incoming branch section.
    """
    resolved = []
    i = 0
    had_conflict = False

    while i < len(lines):
        line = lines[i]

        if line.startswith("<<<<<<<"):
            had_conflict = True
            i += 1

            ours = []
            while i < len(lines) and not lines[i].startswith("======="):
                ours.append(lines[i])
                i += 1

            if i < len(lines) and lines[i].startswith("======="):
                i += 1

            while i < len(lines) and not lines[i].startswith(">>>>>>>"):
                i += 1

            if i < len(lines) and lines[i].startswith(">>>>>>>"):
                i += 1

            resolved.extend(ours)
            continue

        resolved.append(line)
        i += 1

    return resolved, had_conflict

@st.cache_data
def load_data():
    file_path = os.path.join(BASE_DIR, 'bank_churn.csv')
    
    try:
        with open(file_path, "r", encoding="utf-8-sig") as f:
            raw_lines = f.read().splitlines()

        cleaned_lines, had_conflict = _resolve_git_conflicts(raw_lines)
        cleaned_text = "\n".join(cleaned_lines)

        df = pd.read_csv(StringIO(cleaned_text))
        df.columns = [str(col).strip().lower() for col in df.columns]

        # Handle alternative churn naming if needed.
        if "churn" not in df.columns and "exited" in df.columns:
            df = df.rename(columns={"exited": "churn"})

        # Remove accidental repeated header rows that can appear in malformed CSVs.
        if "customer_id" in df.columns:
            df = df[df["customer_id"].astype(str).str.lower() != "customer_id"]

        if "churn" not in df.columns:
            st.error(
                "Error: target column 'churn' is missing in bank_churn.csv. "
                f"Found columns: {list(df.columns)}"
            )
            return None

        df["churn"] = pd.to_numeric(df["churn"], errors="coerce")
        df = df.dropna(subset=["churn"]).copy()
        df["churn"] = df["churn"].astype(int)

        if had_conflict:
            st.warning(
                "Detected and auto-resolved Git merge conflict markers in "
                "bank_churn.csv while loading data."
            )

        return df
    except FileNotFoundError:
        st.error(f"Error: {file_path} not found.")
        return None
    except pd.errors.EmptyDataError:
        st.error(f"Error: {file_path} is empty or invalid.")
        return None
    except Exception as e:
        st.error(f"Unexpected error while loading data: {e}")
        return None


@st.cache_resource
def load_model():
    model_path = os.path.join(BASE_DIR, 'models', 'churn_prediction_model.pkl')
    
    try:
        model = joblib.load(model_path)
        return model
    except FileNotFoundError:
        st.error(f"Error: {model_path} not found.")
        return None
