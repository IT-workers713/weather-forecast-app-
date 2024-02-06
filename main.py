import streamlit as st
import plotly.express as px

st.title("weather forecast app data")


place = st.text_input("place: ")
days = st.slider(" forecast days" ,min_value=1,max_value=5,help=" select the number of forcasted days")
option = st.selectbox("select data to view ",
                      ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_data(days):
    dates=["2020-25-10","2020-25-12","2020-25-11"]
    temperatures=[10,11,15]
    temperatures = [days * i for i in temperatures]
    return dates,temperatures


d,t = get_data(days)

figure = px.line(x=d ,y=t , labels={"x":"dates","y":"temperatues (c)"})
st.plotly_chart(figure)