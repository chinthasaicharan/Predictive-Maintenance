import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import  seaborn as sns
import plotly.graph_objects as go
st.set_page_config(page_title="OPERATOR DASHBOARD", page_icon=":bar_chart:", layout="wide")
st.title("Dashboard")
DATE_COLUMN = 'date/time'
DATA_URL = ('test_data_V1.csv')

st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)
st.markdown("""
<style>
.big-font {
    font-size:300px !important;
}
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.drop(["Type", "Machinebrk", "3"], axis=1, inplace=True)

    return data


data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(200)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')






left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Shot Pressure:")
    st.subheader(f" {data.iloc[-1]['shot_pressure']} MPa ")
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value= data.iloc[-1]['shot_pressure'],
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Shot Pressure"}))
    fig.update_layout(
        autosize=True,
        width=300,
        height=300)
    st.plotly_chart(fig,use_container_width=True)
with middle_column:
    st.subheader("Melt Temperature:")
    st.subheader(f" {data.iloc[-1]['melt_temp']} deg C ")

    line_plot = px.line(data,x="s_no",y="melt_temp",title="Variation of Melt Temperature")
    line_plot.update_layout(
                   xaxis_title='S_no',
                   yaxis_title='Melt Temperature (degrees C)')
    st.plotly_chart(line_plot)
with right_column:
    st.subheader("Die Temperature:")
    st.subheader(f" {data.iloc[-1]['die_temp']} deg C ")


left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Machine Status")
    if data.iloc[-1]['machine_vibration'] < 80:
        st.write("""# Good""")
    elif data.iloc[-1]['machine_vibration'] < 160:
        st.write("""# Average""")
    else:
        st.write("""# Bad""")


with middle_column:
    st.subheader("Part Quality:")
    st.write("""# No Defect""")

with right_column:
    st.subheader("Estimated number of shots before breakdown:")
    st.write("""# 7""")














