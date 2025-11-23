import streamlit as st
import plotly.express as px
from backend import get_data

# Setting up web app title
st.title('Weather Forecast for the next days')
# Adding place input box
place = st.text_input("Place: ")
# Adding slider for day selection
days = st.slider(
    "Forecast days",
    min_value=1,
    max_value=5,
    help="Number of forecasted days")
# Adding selection bax for type of data selection
options = st.selectbox("Select data you want to view", ("Temperature", "Sky"))
# Subheader to make it easier for user to understand what is being displayed
st.subheader(f"{options} for the next {days} days in {place}")

get_data(place, days, options)

# Creating plotly figure
figure = px.line(x=d, y=t, labels={"x": "dates", "y": "Temperature (C)"})
# Adding graph
st.plotly_chart(figure)
