import streamlit as st
import plotly.express as px

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


def get_data(days):
    dates = ["22.11", "23.11", "24.11", "25.11", "26.11"]
    temperatures = [2, 23, 6, 5, 10]
    temperatures = [days*i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)
# Creating plotly figure
figure = px.line(x=d, y=t, labels={"x": "dates", "y": "Temperature (C)"})
# Adding graph
st.plotly_chart(figure)
