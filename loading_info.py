import streamlit as st
import pandas as pd 
import os 
import json 

st.markdown("# Loading Financial Info")

category_file = 'categories.json'

if 'categories' not in st.session_state:
    st.session_state.categories = { 
        'Uncategorized': []
    } 

if os.path.exists(category_file):
    with open(category_file, 'r') as f:
        st.session_state.categories = json.load(f)

def save_categories(): 
    with open(category_file, 'w') as f:
        json.dump(st.session_state.categories, f)

def categorize_transactions(dataframe): 
    dataframe['Category'] = 'Uncategorized'

    for category, keywords in st.session_state.categories.items():
        if category == 'Uncategorized' or not keywords: 
            continue
       
        lowered_keywords = [keyword.lower().strip() for keyword in keywords]

        for idx, row in dataframe.iterrows():
            details = row['Details'].lower().strip()
            if details in lowered_keywords: 
                dataframe.at[idx, 'Category'] = category

    return dataframe

def add_keyword_to_category(category, keyword): 
    keyword = keyword.strip() 
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)
        save_categories()
        return True 
    
    return False 

def load_file(file):
    try: 
        df = pd.read_csv(file, delimiter=';')
        df['Amount'] = df['Amount'].str.replace(',', '.').astype(float)
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True) 
        st.session_state['dataframe'] = categorize_transactions(df)
        return categorize_transactions(df)
    
    except Exception as e: 
        return None
    
def show_edited_dataframe(): 
    edited_df = st.data_editor(
            st.session_state.dataframe[['Date', 'Details', 'Amount', 'Currency', 'Debit/Credit', 'Category']],
            column_config={
                "Date": st.column_config.DateColumn('Date', format='DD/MM/YYYY'),
                "Amount": st.column_config.NumberColumn('Amount', format="%.2f"),
                "Category": st.column_config.SelectboxColumn(
                    "Category", 
                    options=list(st.session_state.categories.keys())
                )
            },
            key='Category_editor'
        )
    return edited_df

def apply_categorie_changes(dataframe):
    save_button = st.button("Apply Changes", type='primary')
    if save_button: 
        for idx, row in dataframe.iterrows():
            new_category = row["Category"]
            if new_category == st.session_state.dataframe.at[idx, 'Category']: 
                continue
            
            details = row['Details']
            st.session_state.dataframe.at[idx, "Category"] = new_category
            add_keyword_to_category(new_category, details)
    return None

def add_category_button(new_category, add_button): 
    if add_button and new_category: 
            if new_category not in st.session_state.categories: 
                st.session_state.categories[new_category] = []
                save_categories()
                st.rerun()
    return None

def main():
    st.divider()
    uploaded_file = st.file_uploader('Financial Data CSV file', type=['csv'])

    if 'dataframe' not in st.session_state:
        df = load_file(uploaded_file) 
        if df is not None:
            new_category_1 = st.text_input('New Category Name')
            add_button_1 = st.button('Add Category')

            edited_df = show_edited_dataframe()
            apply_categorie_changes(edited_df)

            add_category_button(new_category_1, add_button_1)

    else:
        df = st.session_state['dataframe']
        st.write("Pre-loaded DataFrame")

        new_category = st.text_input('New Category Name')
        add_button = st.button('Add Category')

        add_category_button(new_category, add_button)

        st.subheader('Your Expenses')
        edited_df = show_edited_dataframe()
        apply_categorie_changes(edited_df)
        
    # Sidebar Info 
    sidebar_title = st.sidebar.markdown("## Loading Info")
    sidebar_md = st.sidebar.markdown("- This page is dedicated to uploading your financial data through CSV file format, so we can analyse and display your financial dashboard!")

main()