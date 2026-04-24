import streamlit as st
from PIL import Image 


img = Image.open("logo.jpg")

st.image(img,width=600)

st.title("real time price analysis App")

st.header("Daily Price Tracking")
st.header("Historical Storage")
st.header("Price Comparison")
st.header("Alert System for price changes")
st.header("Automated pipeline")

## markdown use for header size increasse decrease(no of # inc so size decrease vice-versa)
st.markdown("### Database Connective")  

st.success("Proceed Successfully")
st.info("Find the formal information")
st.warning("you are going to high risk scenerio")
st.error("Account has been locked for 24 hours")


img = Image.open("logo1.jpg")

st.image(img,width=600)



