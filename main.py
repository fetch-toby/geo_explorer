import streamlit as st
import langchain_helper

st.title("Geo Explorer")

continent = st.sidebar.selectbox("Select a Continent", ["Africa", "Asia", "Australia", "Europe", "North America", "South America"])

if continent:
    response = langchain_helper.get_country_and_cities(continent)
    st.header(response['country'].strip())
    cities = response['cities'].strip().split(',')
    st.write("Cities:")
    for item in cities:
        st.write("-", item)
