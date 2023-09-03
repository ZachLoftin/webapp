import pandas as pd
import streamlit as st
import plotly.express as px
import plotly as pl
import numpy as np
import scipy as sp
import seaborn as sns
from PIL import Image
import matplotlib.pyplot as plt
import os

vehicle_data = pd.read_csv('vehicles_us.csv')

st.title('Vehicle Data Analysis')


st.set_option('deprecation.showPyplotGlobalUse', False)

select_column = st.selectbox('Select a column', vehicle_data.columns)

plt.figure(figsize=(12, 6))

plt.xticks(rotation=45)

sns.histplot(vehicle_data[select_column], kde=True, bins=20)
st.pyplot()

st.write(f"Statistics for {select_column}:")

st.write(vehicle_data[select_column].describe())


