import pandas as pd
import streamlit as st
import plotly.express as px

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

    fig = px.scatter(vehicle_data, x=x_column, y=y_column, title=f"Scatterplot: {x_column} vs {y_column}")
    st.plotly_chart(fig)

else:
    st.subheader(f"Histogram for {select_column}")

    fig = px.histogram(vehicle_data, x=select_column, nbins=20, title=f"Histogram: {select_column}")
    st.plotly_chart(fig)

st.write(f"Statistics for {select_column}:")

st.write(vehicle_data[select_column].describe())


