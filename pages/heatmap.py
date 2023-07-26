import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

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

st.title("Flood Incidents in Malaysia")

button = st.slider("Year", 2015,2022,2022)
data = pd.read_csv('data/Flood Data Updated Geocoded.csv')

if button == 2015:
    data = data[data['Year'] == 2015]
elif button == 2016:
    data = data[data['Year'] == 2016]
elif button == 2017:
    data = data[data['Year'] == 2017]
elif button == 2018:
    data = data[data['Year'] == 2018]
elif button == 2019:
    data = data[data['Year'] == 2019]
elif button == 2020:
    data = data[data['Year'] == 2020]
elif button == 2021:
    data = data[data['Year'] == 2021]
else:
    data = data[data['Year'] == 2022]

with st.expander("Source Code (Click to Expand)"):
    with st.echo():

        filepath = "data/Flood Data Updated Geocoded.csv"
        m = leafmap.Map(center=[4, 108], zoom=5, tiles="stamentoner")
        m.add_heatmap(
            data,
            latitude="Latitude",
            longitude="Longitude",
            name="Heat map",
            value = "Year", # becomes frequency: some place flood a few times in a year, but also affect by reporting duration (data collection part)
            radius=20,
        )


m.to_streamlit(height=700)
