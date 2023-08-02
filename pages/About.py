import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")

st.sidebar.info(
    """
    - GitHub repository: [streamlit_flood](https://github.com/keanteng/streamlit_flood)
    """
)

st.sidebar.title("Created By")
st.sidebar.info(
    """
  Khor Kean Teng
  - Intern, DGA, JPS
    """
)

st.title("Introduction")

st.markdown(
    """
    This is a web app created using streamlit to visualize flood incidents in Malaysia from the year 2015 - 2022. The side bar menu
    provide navigation to different types of maps. The map is interactive, you can zoom in and out, and click on the markers to see.
    """
)

st.info("👈Check out the maps on the list beside to see how the map works")

data = pd.read_csv("data/all_states_all_years_geocoded.csv")
data = pd.DataFrame(data[['Year']],data[['State']])
st.area_chart(data)