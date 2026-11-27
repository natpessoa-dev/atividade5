import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('/content/WHO_time_series.csv')

fig1 = px.line(df, x = 'Date_reported', y = 'Cumulative_cases', color = 'Country',
               title = 'Dados de Covid-19 no mundo - Ano 2020')
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'nº casos acumulados',
                   title_font_size = 30)
fig1.show()


st.set_page_config(page_title='DashCovid', layout='wide')
st.title('DASHCOVID: Um dashboard sobre dados de Covid-19 - Ano 2020')
st.plotly_chart(fig1, use_container_width=True)
