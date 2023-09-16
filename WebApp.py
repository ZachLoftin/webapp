import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np


vehicle_data = pd.read_csv('vehicles_us.csv')

#this cache stores the function, allowing the app to run more smoothly
@st.cache_data
def median_value(group):
    return group.fillna(group.median())

#this group of code adds the median value to any NaN
vehicle_data['model_year'] = vehicle_data.groupby('model')['model_year'].transform(median_value)
vehicle_data['cylinders'] = vehicle_data.groupby('model')['cylinders'].transform(median_value)
vehicle_data['odometer'] = vehicle_data.groupby('model_year')['odometer'].transform(lambda x: x.fillna(x.median()))

#this replaces the names of the columns with more presentable ones
new_column_names = {'price': 'Price', 'model_year': 'Model Year', 'model': 'Model', 'condition': 'Condition', 'cylinders': 'Cylinders', 'fuel': 'Fuel',
                    'odometer': 'Odometer', 'transmission': 'Transmission', 'type': 'Type', 'paint_color': 'Paint Color', 'is_4wd': 'Has 4WD', 'date_posted': 'Date Posted',
                    'days_listed': 'Days Listed'}
vehicle_data.rename(columns=new_column_names, inplace=True)

st.title('Vehicle Data Analysis Tool')

st.set_option('deprecation.showPyplotGlobalUse', False)

select_model = st.selectbox('Select a car model', vehicle_data['Model'].unique())
filtered_data = vehicle_data[vehicle_data['Model'] == select_model]

st.write('Filtered Data:')
st.write(filtered_data)

st.subheader('Scatterplot for selected car model')
x_column = st.selectbox('Select x-axis column', vehicle_data.columns)
y_column = st.selectbox('Select y-axis column', vehicle_data.columns)

fig = px.scatter(filtered_data, x=x_column, y=y_column, title=f"Scatterplot: {x_column} vs {y_column}")
st.plotly_chart(fig)

st.subheader('Histogram for selected car model')
fig = px.histogram(filtered_data, x=x_column, nbins=20, title=f"Histogram: {x_column}")
st.plotly_chart(fig)

st.write(f"Statistics for {x_column}:")
st.write(filtered_data[x_column].describe())

#this is the title of the web app and is displayed at the top of the page
#st.title('Vehicle Data Analysis Tool')

#st.set_option('deprecation.showPyplotGlobalUse', False)

#this is a dropdown menu that allows the user to select any column of the dataset to view as a histogram
#select_column = st.selectbox('Select a column', vehicle_data.columns)
#checking this box will change the histogram to a scatterplot, allowing you to compare 2 different columns
#scatterplot_option = st.checkbox("Show a Scatterplot", False)

#this if/else statement sets up the checkbox. If the check box isn't selected, it shows a histogram. 
#If the checkbox IS selected, it shows a scatterplot.
#if scatterplot_option:
#    st.subheader(f'Scatterplot for {select_column}')
#    x_column = st.selectbox('Select x-axis column', vehicle_data.columns)
#    y_column = st.selectbox('Select y-axis column', vehicle_data.columns)

#    fig = px.scatter(vehicle_data, x=x_column, y=y_column, color=select_column, title=f"Scatterplot: {x_column} vs {y_column}")
#    st.plotly_chart(fig)

#else:
#    st.subheader(f"Histogram for {select_column}")

#    fig = px.histogram(vehicle_data, x=select_column, nbins=20, title=f"Histogram: {select_column}")
#    st.plotly_chart(fig)

#This will show the general statistics for the columns displayed
#st.write(f"Statistics for {select_column}:")

#st.write(vehicle_data[select_column].describe())


