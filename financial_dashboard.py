import streamlit as st
import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns 
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

st.markdown("# Financial Dashboard")

def get_sum(dataframe,  start_date, end_date):
    filtered_df = get_interval_dataframe(dataframe, start_date, end_date)
    result = filtered_df['Amount'].sum()
    formated_result = locale.currency(result, grouping=True)
    show_result = st.markdown(f'## Total Spent: {formated_result}')
    return show_result

def get_interval_dataframe(dataframe, start_date, end_date):
    mask = (dataframe['Date'] >= pd.to_datetime(start_date)) & (dataframe['Date'] <= pd.to_datetime(end_date))
    filtered_df = dataframe.loc[mask]
    return filtered_df 

def show_graph_total_amount_category(dataframe, start_date, end_date): 
    filtered_df = get_interval_dataframe(dataframe, start_date, end_date)
    grouped_df = filtered_df.groupby('Category').Amount.sum().reset_index()
    st.bar_chart(grouped_df, x='Category', y='Amount', x_label='Category', y_label='Total Amount')

def show_graph_mean_amount_category(dataframe, start_date, end_date): 
    filtered_df = get_interval_dataframe(dataframe, start_date, end_date)
    grouped_df = filtered_df.groupby('Category').Amount.mean().reset_index()
    st.bar_chart(grouped_df, x='Category', y='Amount', x_label='Category', y_label='Mean Amount')

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
            col_1, col_2 = st.columns(2)
            with col_1: 
                start_date_credit = st.date_input('Initial Date C', df['Date'].min().date())
            with col_2: 
                end_date_credit = st.date_input('Final Date C', df['Date'].max().date())  

            get_sum(df_credit, start_date_credit, end_date_credit)

            sub_col_1, sub_col_2 = st.columns(2)
            with sub_col_1:
                show_graph_total_amount_category(df_credit, start_date_credit, end_date_credit)
            with sub_col_2:
                show_graph_mean_amount_category(df_credit, start_date_credit, end_date_credit)
            st.dataframe(get_interval_dataframe(df_credit, start_date_credit, end_date_credit))
        with tab2: 
            col_3, col_4 = st.columns(2)
            with col_3: 
                start_date_debit = st.date_input('Initial Date D', df['Date'].min().date())
            with col_4: 
                end_date_debit = st.date_input('Final Date D', df['Date'].max().date())  

            get_sum(df_debit, start_date_debit, end_date_debit)

            sub_col_3, sub_col_4 = st.columns(2)
            with sub_col_3:
                show_graph_total_amount_category(df_debit, start_date_debit, end_date_debit)
            with sub_col_4:
                show_graph_mean_amount_category(df_debit, start_date_debit, end_date_debit)
            st.dataframe(get_interval_dataframe(df_debit, start_date_debit, end_date_debit))

    # Sidebar Info 
    sidebar_title = st.sidebar.markdown("## Financial Dashboard")
    sidebar_mds = st.sidebar.markdown("- Here you can visualize and analyse your financial data with accurary!")

main()