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
new_column_names = {'price': 'Price', 'model_year': 'Model Year', 'model': 'Model', 'condition': 'Condition', 'cylinders': 'Cylinders', 'fuel': 'Fuel',
                    'odometer': 'Odometer', 'transmission': 'Transmission', 'type': 'Type', 'paint_color': 'Paint Color', 'is_4wd': 'Has 4WD', 'date_posted': 'Date Posted',
                    'days_listed': 'Days Listed'}
vehicle_data.rename(columns=new_column_names, inplace=True)

st.title('Vehicle Data Analysis Tool')

st.set_option('deprecation.showPyplotGlobalUse', False)

select_column = st.selectbox('Select a column', vehicle_data.columns)
scatterplot_option = st.checkbox("Show a Scatterplot", False)

if scatterplot_option:
    st.subheader(f'Scatterplot for {select_column}')
    x_column = st.selectbox('Select x-axis column', vehicle_data.columns)
    y_column = st.selectbox('Select y-axis column', vehicle_data.columns)

    plt.figure(figsize=(12,6))
    sns.scatterplot(x=x_column, y=y_column, data=vehicle_data)
    plt.title(f"Scatterplot: {x_column} vs {y_column}")
    plt.xticks(rotation=45)
    st.pyplot()
else:
    st.subheader(f"Histogram for {select_column}")
    
    plt.figure(figsize=(16, 6))
    sns.histplot(vehicle_data[select_column], kde=True, bins=20)
    plt.title(f"Histogram: {select_column}")
    st.pyplot()


st.write(f"Statistics for {select_column}:")

st.write(vehicle_data[select_column].describe())


