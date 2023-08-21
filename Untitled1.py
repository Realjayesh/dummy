#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import folium
import random

# Page 1: Home
def home():
    st.title("Home")
    st.write("Welcome to the random map app!")

# Page 2: Map 1
def map1():
    st.title("Map 1")
    st.write("This is a random map.")

    # Generate a random location
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)

    # Create a Folium map
    m = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker([lat, lon], popup='Random Location').add_to(m)

    # Display the map using the folium_to_streamlit utility
    st.write(m._repr_html_(), unsafe_allow_html=True)

# Page 3: Map 2
def map2():
    st.title("Map 2")
    st.write("This is another random map.")

    # Generate a random location
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)

    # Create a Folium map
    m = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker([lat, lon], popup='Random Location').add_to(m)

    # Display the map using the folium_to_streamlit utility
    st.write(m._repr_html_(), unsafe_allow_html=True)

# Main app
def main():
    st.sidebar.title("Navigation")
    pages = {
        "Home": home,
        "Map 1": map1,
        "Map 2": map2,
    }
    selected_page = st.sidebar.radio("Go to", list(pages.keys()))
    pages[selected_page]()

if __name__ == "__main__":
    main()

