import streamlit as st
from pages.charts.avg_price import display_avg_prices

st.set_page_config(layout="wide")

st.title('CPI (Consumer Price Index)', text_alignment='center')

avg_prices, other = st.tabs(['Avg Prices', 'Other'])

with avg_prices:
    display_avg_prices()
with other:
    st.text("TODO")