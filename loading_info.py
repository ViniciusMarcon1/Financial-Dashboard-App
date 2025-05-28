import streamlit as st
import pandas as pd 
import os 
import json 

# Title 
st.markdown("# Loading Financial Info 💵")

category_file = 'categories.json'

if 'categories' not in st.session_state:
    st.session_state.categories = { 
        'Uncategorized': []
    } 

# Loading Categories into Session State 
if os.path.exists(category_file):
    with open(category_file, 'r') as f:
        st.session_state.categories = json.load(f)

# Saving Categories into File from Session State  
def save_categories(): 
    with open(category_file, 'w') as f:
        json.dump(st.session_state.categories, f)

def display_sidebar_info():
    sidebar_title = st.sidebar.markdown("## Loading Info")
    sidebar_md = st.sidebar.markdown("- This page is dedicated to uploading your financial data through CSV file format, so we can analyse and display your financial dashboard!")
    return sidebar_title, sidebar_md

# Categorize Transactions Based on the Description name in the CSV is in the 'categories.json' 
def categorize_transactions(dataframe): 
    dataframe['Category'] = 'Uncategorized'

    for category, keywords in st.session_state.categories.items():
        if category == 'Uncategorized' or not keywords: 
            continue
       
        lowered_keywords = [keyword.lower().strip() for keyword in keywords]

        # Iteration throw dataframe to check if description name match item in categories 
        for idx, row in dataframe.iterrows():
            details = row['Details'].lower().strip()
            if details in lowered_keywords: 
                dataframe.at[idx, 'Category'] = category

    return dataframe

# Define button to add new category into categories and saves it    
def add_category_button(): 
    new_category = st.text_input('New Category Name')
    add_button = st.button('Add Category')
    if add_button and new_category: 
            if new_category not in st.session_state.categories: 
                st.session_state.categories[new_category] = []
                save_categories()
                st.rerun()
    return None

# Adding new keyword into a category and calling save categories 
def add_keyword_to_category(category, keyword): 
    keyword = keyword.strip() 
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)
        save_categories()
        return True 
    
    return False 

# Loading CSV File, cleaning and loading into dataframe 
def load_file(file):
    try: 
        df = pd.read_csv(file, delimiter=';')
        # Turn amount from string to float 
        df['Amount'] = df['Amount'].str.replace(',', '.').astype(float)
        # Turn date into timestamp 
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True) 
        # Saving dataframe into Session State after categorizing each Transaction
        st.session_state['dataframe'] = categorize_transactions(df)
        return categorize_transactions(df)
    
    except Exception as e: 
        return None

# Turn dateframe into data editor format 
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

# Call function 'add_keyword_to_category based on button action 
def apply_categorie_changes(dataframe):
    save_button = st.button("Apply Changes")
    if save_button: 
        # Iterating throw dataframe to apply new category into each transaction 
        for idx, row in dataframe.iterrows():
            new_category = row["Category"]
            if new_category == st.session_state.dataframe.at[idx, 'Category']: 
                continue
            
            details = row['Details']
            st.session_state.dataframe.at[idx, "Category"] = new_category
            add_keyword_to_category(new_category, details)
    return None


def list_unique_transactions(dateframe): 
    set_sample = dateframe['Details'].unique()
    return set_sample

# Main menu that displays what is seen on screen when runing the app 
def main():
    st.divider()
    uploaded_file = st.file_uploader('Financial Data CSV file', type=['csv'])

    if 'dataframe' not in st.session_state:
        df = load_file(uploaded_file) 
        if df is not None:

            add_category_button()
            st.subheader('Your Expenses')
            edited_df = show_edited_dataframe()
            apply_categorie_changes(edited_df)           

    else:
        df = st.session_state['dataframe']
        st.write("Pre-loaded DataFrame")

        add_category_button()

        st.subheader('Your Expenses')
        edited_df = show_edited_dataframe()
        apply_categorie_changes(edited_df)
        
    # Sidebar Info 
    display_sidebar_info()

main()