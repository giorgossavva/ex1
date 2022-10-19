import streamlit as st

PAGES = {
    "About us": existing_data
}

st.set_page_config(page_title="Covid19-Cyprus", page_icon="🧊", layout='wide', initial_sidebar_state='auto')
st.sidebar.title('🧭 Navigation')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.streamlit_app()
