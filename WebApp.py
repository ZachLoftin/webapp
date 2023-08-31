import pandas as pd
import streamlit as st
import plotly as pl
import os

#csv_file_path = os.path.join(os.path.dirname(__file__), 'vehicles_us.csv')

vehicle_data = pd.read_csv('vehicles_us.csv')

print(vehicle_data.head(20))