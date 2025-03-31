import pandas as pd
import numpy as np
import streamlit as st
import pandaslib as pl
  
#TODO Write your extraction code here

# This is to read the google sheet csv file
survey = pd.read_csv('https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/export?resourcekey=&gid=1625408792&format=csv')
# This is to extract year from date creating a new column called year, extract_year_mdy is a function in pandaslib
survey['year'] = survey['Timestamp'].apply(pl.extract_year_mdy)
# save the survey data to csv file
survey.to_csv('cache/survey.csv', index=False)
# get each unique year in the data
year = survey['year'].unique()

years = survey['year'].unique()
for year in years:
    col_year = pd.read_html(f"https://www.numbeo.com/cost-of-living/rankings.jsp?title={year}&displayColumn=0")
    col_year = col_year[1]
    col_year['year'] = yearcol_year.to_csv(f'cache/col_{ear}.csv', index=False)   

states = pd.read_csv("https://docs.google.com/spreadsheets/d/14wvnQygIX1eCVo7H5B7a96W1v5VCg6Q9yeRoESF6epw/export?format=csv")
states.to_csv('cache/states.csv', index=False)