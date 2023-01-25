import streamlit as st
import plotly.express as px
from backend import get_data

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


if place != "":
    try:
        data = get_data(place, days)
        dates = [dict["dt_txt"] for dict in data]
        if select == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in data]
            figure = px.line(
                x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperature"}
            )
            st.subheader(f"{select} for the next {days} {day} in {place}")
            st.plotly_chart(figure)

        if select == "Sky":
            columns = st.columns(6)
            
            conditions = [dict["weather"][0]["icon"] for dict in data]
            for d,i,col in zip(dates,conditions,range(len(dates))):
                with columns[col%6]:
                    st.image(f"http://openweathermap.org/img/w/{i}.png",caption=d,use_column_width="always")
    except KeyError:
        st.write("<p style='color:red'>GIVEN CITY DOES NOT EXIST! Please correct city name.</p>",unsafe_allow_html=True)        

            