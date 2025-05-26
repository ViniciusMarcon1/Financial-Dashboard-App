import streamlit as st
import pandas as pd 
import plotly as pt 
import numpy as np
import locale

# Configura o locale para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

st.markdown("# Financial Dashboard")

def get_sum(dataframe):
    result = dataframe['Amount'].sum()
    formated_result = locale.currency(result, grouping=True)
    show_result = st.markdown(f'## Total Spent: {formated_result}')
    return show_result

def main():
    st.divider()

    # Checking for Loaded Data
    if 'dataframe' in st.session_state: 
        df = st.session_state['dataframe']
        df_debit = df[df['Debit/Credit'] == 'Debit'].copy()
        df_credit = df[df['Debit/Credit'] == 'Credit'].copy()

        # Separating diferent Debit/Credit values into diferent tabs 
        tab1, tab2 = st.tabs(['Credit Info', 'Debit Info'])
        with tab1:    
            get_sum(df_credit)
            st.dataframe(df_credit)
        with tab2: 
            get_sum(df_debit)
            st.dataframe(df_debit)

    # Sidebar Info 
    sidebar_title = st.sidebar.markdown("## Financial Dashboard")
    sidebar_mds = st.sidebar.markdown("- Here you can visualize and analyse your financial data with accurary!")

main()