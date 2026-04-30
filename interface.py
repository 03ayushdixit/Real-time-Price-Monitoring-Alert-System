import streamlit as st
from PIL import Image 
import pandas as pd
import requests
import plotly.express as px

img = Image.open("logo.jpg")

# Resize the image (width, height)
img = img.resize((1000, 200))   # Increase size

st.image(img,width=600)

st.set_page_config(page_title="Fake Store Insights", page_icon="🏤",layout="wide")
st.title("🏤 Fake Store API - Interactive Dashboard")

Api="https://fakestoreapi.com/products"

@st.cache_data
def load_data():
    response=requests.get(Api)
    data=response.json()
    df=pd.DataFrame(data)
    return df
df=load_data()
st.subheader(" 🛣 dataset Overview")
st.dataframe(df,use_container_width=True)

# basic cleaning

df['price']= df['price'].astype(float)
df['category']= df['category'].astype(str)

# slider
st.sidebar.header("🚥 Filters")
categories= st.sidebar.multiselect(
    "Select Category",
    df["category"].unique(),default=df["category"].unique()
)

filtered_df = df[df['category'].isin(categories)]

# KPI 

st.header(" 📍 Key Insights ")

col1,col2,col3 = st.columns(3)

col1.metric("Total products ",len(filtered_df))
col2.metric("Average Price ",f"${filtered_df['price'].mean():.2f}")
col3.metric("Highest Price ",f"${filtered_df['price'].max():.2f}")

#Visuals

st.header(" 🎁 Key Insights")

# bar chart -: category count 

cate_count= filtered_df["category"].value_counts().reset_index()
cate_count.columns = ["category", "count"]
fig_bar=px.bar(cate_count, x="category",y="count",title="Products count by category")
st.plotly_chart(fig_bar,use_container_width=True)

# Price Distribution
fig_hist=px.histogram(filtered_df,x='price',nbins=20,title="Price Distribution")
st.plotly_chart(fig_hist,use_container_width=True)   

# Scattered Price Vs ID

fig_scatter=px.scatter(filtered_df,x="id",y="price",
                       color="category",title="Price by Product Id")

st.plotly_chart(fig_scatter,use_container_width=True)


# Table view

st.header("Filtered product")
st.dataframe(filtered_df,use_container_width=True)


# Download button 
csv= filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("Download  Filtered Data (csv)",csv,
                   "filtered_data.csv",
                   "text/csv"
                   )










