import streamlit as st

st.title('Weather Forecast for the next days')
place = st.text_input("Place: ")
days = st.slider(
    "Forecast days",
    min_value=1,
    max_value=5,
    help="Number of forecasted days")
options = st.selectbox("Select data you want to view", ("Temperature", "Sky"))
st.subheader(f"{options} for the next {days} days in {place}")

