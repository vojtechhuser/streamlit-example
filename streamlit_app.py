import pandas as pd
import pygwalker as pyg

import streamlit as st
import streamlit.components.v1 as components

title = 'Principal Investigators data aggregated by year (2016-2022)'

st.set_page_config(
    page_title=title,
    layout='wide'
)

st.title(title)
st.markdown(" <style> div[class^='block-container'] { padding-top: 2rem; } </style> ", unsafe_allow_html=True)
df = pd.read_csv('01-PIs.csv.gz')
pyg_html = pyg.to_html(df)
components.html(pyg_html, height=1000, scrolling=True)
