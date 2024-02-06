import streamlit as st
import plotly.express as px
from backend import get_data
st.title("weather forecast app data")
#deployement dans weather

place = st.text_input("place: ")
days = st.slider(" forecast days" ,min_value=1,max_value=5,help=" select the number of forcasted days")
option = st.selectbox("select data to view ",
                      ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


if place:


    filtred_data = get_data(place,days)

    if option =="Temperature":
        temperatues = [dict["main"]["temp"] for dict in filtred_data]
        dates = [dict["dt_txt"] for dict in filtred_data]
        figure = px.line(x=dates, y=temperatues, labels={"x": "dates", "y": "temperatues (c)"})
        st.plotly_chart(figure)
    if option =="Sky":
        images = {"Clear":"images/clear.png","Clouds":"images/cloud.png","Rain":"images/rain.png","Snow":"images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtred_data]
        image_paths = [images[condition] for condition in sky_conditions]
        print(sky_conditions)
        st.image(image_paths,width=115)
