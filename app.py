import streamlit as st

pg = st.navigation([
    st.Page("pages/cpi.py", title="CPI"),
    st.Page("pages/inflation.py", title="Inflation")
])

pg.run()