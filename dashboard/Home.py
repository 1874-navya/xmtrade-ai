import streamlit as st

st.set_page_config(page_title="XMTrade AI", layout="wide")
st.title("XMTrade AI")
st.caption("Gold intraday research • PAPER TRADING ONLY")
st.warning("No broker orders are placed. All trades are simulated.")
a, b, c = st.columns(3)
a.metric("Paper starting balance", "$1,000.00")
b.metric("Primary timeframe", "M15")
c.metric("Risk ceiling", "0.5%")
st.info("No live market feed is configured in this starter scaffold.")
