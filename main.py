import streamlit as st
import pandas as pd 
import plotly as pt 
import financial_dashboard, ask_ai

main_page = st.Page("loading_info.py", title="Main Page", icon="💾")
financial_page = st.Page("financial_dashboard.py", title="Page 2", icon="💵")
ai_page = st.Page("ask_ai.py", title="Page 3", icon="🤖")

pg = st.navigation([main_page, financial_page, ai_page])

# Run the selected page
pg.run()
