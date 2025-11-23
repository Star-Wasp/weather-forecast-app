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
st.subheader(f"{options} for the next {days} days in {place.title()}")
if place:
    try:
        # Get Temperature/Sky data
        filtered_data = get_data(place, days)

        if options == "Temperature":
            # Getting temperature data
            temperatures = [dict["main"]["temp"]-273.15 for dict in filtered_data]
            # Getting days
            days = [dict["dt_txt"] for dict in filtered_data]
            # Creating a temperature plot
            figure = px.line(x=days, y=temperatures, labels={"x": "dates", "y": "Temperature (C)"})
            # Adding graph
            st.plotly_chart(figure)

        if options == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            # Making dictionary of image filepaths
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        message = f"I'm sorry but {place.title()} does not exist. Please try again 😉"
        st.write(message)
