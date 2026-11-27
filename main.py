import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='DashCovid', layout='wide')
st.title('DASHCOVID: Um dashboard sobre dados de Covid-19 - Ano 2020')

df = pd.read_csv('WHO_time_series.csv')

df['Date_reported'] = pd.to_datetime(df['Date_reported'])

fig1 = px.line(df, x = 'Date_reported', y = 'Cumulative_cases', color = 'Country',
               title = 'Dados de Covid-19 no mundo - Ano 2020')
fig1.update_layout(xaxis_title = 'Data', yaxis_title = 'nº casos acumulados',
                   title_font_size = 30)
fig1.show()

st.plotly_chart(fig1, use_container_width=True)

filtro1 = df.query('Country == "Brazil" or Country == "United States of America"')

fig2 = px.line(filtro1, x = 'Date_reported', y = 'Cumulative_cases', color = 'Country',
               title = 'Dados de Covid-19: Brasil x EUA')
fig2.update_layout(xaxis_title = 'Data', yaxis_title = 'nº casos acumulados',
                   title_font_size = 30)
fig2.show()

st.plotly_chart(fig2, use_container_width=True)
