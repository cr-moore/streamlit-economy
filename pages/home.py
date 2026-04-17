import streamlit as st

st.markdown("""
    Economy Diconomy:
""")

st.markdown("""
    The economy is one of the most talked about — and least understood — topics
    in modern politics. Everyone has an opinion. Not everyone has the data.
""")

st.markdown("""
    Economy Diconomy is a no-spin, no-agenda dashboard built on one simple idea:
    **let the numbers speak for themselves.**

    We pull directly from the U.S. Bureau of Labor Statistics — the same source
    economists, policymakers, and journalists use — and present it as plainly as
    possible. No commentary. No framing. Just the data, visualized clearly so you
    can draw your own conclusions.

    Whether prices are up, down, or somewhere in between, you deserve to see it
    for yourself.

    Pick a topic and see what the numbers actually show.
""")

st.markdown("---")


if st.button("CPI (Consumer Price Index)", use_container_width=False):
    st.switch_page("pages/cpi.py")
if st.button("Inflation", use_container_width=False):
    st.switch_page("pages/inflation.py")