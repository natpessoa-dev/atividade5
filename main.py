import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='DashCovid', layout='wide')
st.title('DASHCOVID: Um dashboard sobre dados de Covid-19 - Ano 2020')

df = pd.read_csv('/content/WHO_time_series.csv')
