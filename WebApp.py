import pandas as pd
import streamlit as st
import plotly.express as px
import plotly as pl
import numpy as np
import scipy as sp
import seaborn as sns
from PIL import Image
import os

vehicle_data = pd.read_csv('vehicles_us.csv')

st.title('Vehicle Data Analysis')

#st.sidebar.header("Settings")

#bins = st.sidebar.slider("Number of Bins", 1, 100, 20)

histo = px.histogram(vehicle_data, x='model')

st.plotly_chart(histo)
