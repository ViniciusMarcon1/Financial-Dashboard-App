import streamlit as st

st.markdown("# Ask AI 🤖")

def show_sidebar_info():
    sidebar_title = st.sidebar.markdown("## Ask AI")
    sidebar_md = st.sidebar.markdown("- Ask AI any question about your spending and earning habits! The AI is feed all your financial situation and dashboard visualizations so it can help you achive your financial goals!")
    return sidebar_title, sidebar_md

def main():
    st.divider()
    
    # Sidebar Info 
    show_sidebar_info()

main()