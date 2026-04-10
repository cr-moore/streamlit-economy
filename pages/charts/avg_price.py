import streamlit as st
import pandas as pd
import altair as alt
from util.retrieve_data import get_data


def display_avg_prices():
    #Avg Price Summary
    with st.container(border=True):
        st.text("Data gathered from the U.S. Bureau of Labor Statistics. \nThe chart below contains the average prices of consumer goods each month of the year. \nFiltering to one item will show the percentage change for the selected time range.")

    # read csv data
    @st.cache_data
    def load_data():
        try:
            return pd.read_csv('datafolder/cpi_data.csv')
        except:
            get_data()
            return pd.read_csv('datafolder/cpi_data.csv')


    # Convert date column
    df = load_data()
    df['date'] = pd.to_datetime(df['date'])


    # Layout: filters on left, chart on right
    filter_col, chart_col = st.columns([1, 3])

    with filter_col:
        with st.container(border=True, height='stretch'):
            st.subheader('Filters')

            all_items = sorted(df['item'].unique())
            selected_items = st.multiselect(
                'Item',
                options=all_items,
                default=all_items
            )

            min_date = df['date'].min().to_pydatetime()
            max_date = df['date'].max().to_pydatetime()

            start_date, end_date = st.slider(
                'Date Range',
                min_value=min_date,
                max_value=max_date,
                value=(min_date, max_date),
                format='MMM YYYY'
            )

    # Apply filters
    if selected_items:
        df = df[df['item'].isin(selected_items)]
    df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]


    with chart_col:
        # KPI - percent change if single item selected
        if len(selected_items) == 1:
            item_df = df[df['item'] == selected_items[0]].sort_values('date')
            first_val = item_df['value'].iloc[0]
            last_val = item_df['value'].iloc[-1]
            pct_change = ((last_val - first_val) / first_val) * 100

            st.metric(
                label=f"{selected_items[0]}",
                value=f"{pct_change:.2f}%",
                border=True, width='content'
            )

        # PRICE Chart - prices of goods for month/year
        with st.container(border=True):
            chart = alt.Chart(df).mark_line().encode(
                x=alt.X('date:T',
                        scale=alt.Scale(domain=[df['date'].min().strftime('%Y-%m-%d'), df['date'].max().strftime('%Y-%m-%d')]),
                        axis=alt.Axis(tickCount='month', format='%b %Y')),
                y='value:Q',
                color='item:N',
            )
            st.altair_chart(chart, width='stretch', height='stretch')


    if st.button("Show Table"):
        st.write(df.reset_index(drop=True))