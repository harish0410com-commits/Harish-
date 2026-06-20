import streamlit as st
import pandas as pd

st.title("Buyer Segmentation Dashboard")
st.write("Welcome, Harish! Your app is successfully deployed.")

# Upload output file to check
uploaded_file = st.file_uploader("Upload your Buyer_Segmentation_Output (1).xls file", type=["xls", "xlsx"])
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())
