import streamlit as st

st.set_page_config(page_title='Personal Financial Dashboard', page_icon='🤑', layout='wide')

loading_info = st.Page("loading_info.py", title="Loading", icon="💾")
financial_page = st.Page("financial_dashboard.py", title="Dashboard", icon="💵")
ai_page = st.Page("ask_ai.py", title="Ask AI", icon="🤖")

pg = st.navigation([loading_info, financial_page, ai_page])

# Run the selected page
pg.run()
