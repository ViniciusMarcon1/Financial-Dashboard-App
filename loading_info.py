import streamlit as st
import pandas as pd 
import plotly as pt 
import numpy as np

st.markdown("# Loading Financial Info")

def load_file(file):
    try: 
        df = pd.read_csv(file, delimiter=';')
        df['Amount'] = df['Amount'].str.replace(',', '.').astype(float)
        st.dataframe(df)
        st.session_state['dataframe'] = df
        return df
    except Exception as e: 
        return None

def main():
    st.divider()
    uploaded_file = st.file_uploader('Financial Data CSV file', type=['csv'])

    if 'dataframe' not in st.session_state:
        df = load_file(uploaded_file)
    else:
        df = st.session_state['dataframe']
        st.write("Pre-loaded DataFrame")
        st.dataframe(df)


    # Sidebar Info 
    sidebar_title = st.sidebar.markdown("## Loading Info")
    sidebar_md = st.sidebar.markdown("- This page is dedicated to uploading your financial data through CSV file format, so we can analyse and display your financial dashboard!")

main()