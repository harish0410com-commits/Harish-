import streamlit as st
import pandas as pd

st.title("Buyer Segmentation Dashboard")
st.write("Welcome, Harish! Your app is successfully deployed.")

uploaded_file = st.file_uploader("Upload your file", type=["xls", "xlsx", "csv"])
if uploaded_file is not None:
    try:
        # Intha single line prachanaiye solve pannidum!
        df = pd.read_csv(uploaded_file)
        st.write("### Data Preview")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error: {e}")
