import streamlit as st

day = "day"

st.header("Weather Forecast for the next days")

place = st.text_input(label="Place:")

days = st.slider(
    label="Forecast Days",
    min_value=1,
    max_value=5,
    help="Select the number of forecasted days",
)

if days != 1:
    day = "days"

select = st.selectbox(label="Select data to view", options=("Temperature", "Sky"))

st.subheader(f"{select} for the next {days} {day} in {place}")
