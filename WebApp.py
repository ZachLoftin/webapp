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

#title for web page
st.title('Vehicle Data Analysis Tool')

st.set_option('deprecation.showPyplotGlobalUse', False)

#this allows us to select the car model for further analysis
select_model = st.selectbox('Select a car model', vehicle_data['Model'].unique())
filtered_data = vehicle_data[vehicle_data['Model'] == select_model]

#this displays the individual cars of the selected models and the values on each column
st.write('Filtered Data:')
st.write(filtered_data)

#scatterplot for the selected car model and which two columns the user wants to compare
st.subheader('Scatterplot for selected car model')
x_column = st.selectbox('Select x-axis column', vehicle_data.columns)
y_column = st.selectbox('Select y-axis column', vehicle_data.columns)

fig = px.scatter(filtered_data, x=x_column, y=y_column, title=f"Scatterplot: {x_column} vs {y_column}")
st.plotly_chart(fig)

#Histogram for the selected car model and the x-axis selection on the scatterplot section
st.subheader('Histogram for selected car model')
fig1 = px.histogram(filtered_data, x=x_column, nbins=20, title=f"Histogram: {x_column}")
st.plotly_chart(fig1)

#Scatterplot to compare two different car brands by price and odometer
car_models = st.multiselect('Choose car models for comparison', vehicle_data['Model'].unique())
filtered_models = vehicle_data[vehicle_data['Model'].isin(car_models)]

st.subheader('Scatterplot for selected car models')
fig2 = px.scatter(filtered_models, x='Odometer', y='Price', color='Model', title='Scatterplot: Odometer vs Price',
                 labels={'Odometer': 'Odometer (miles)', 'Price': 'Price ($$$)'})
st.plotly_chart(fig2)

st.write(f"Statistics for {x_column}:")
st.write(filtered_data[x_column].describe())


