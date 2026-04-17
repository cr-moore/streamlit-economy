import streamlit as st

st.set_page_config(page_title='Economy Diconomy')

pg = st.navigation([
    st.Page("pages/Home.py", title="Home"),
    st.Page("pages/cpi.py", title="CPI"),
    st.Page("pages/inflation.py", title="Inflation"),
    st.Page('pages/settings.py', title='Settings')
])

pg.run()