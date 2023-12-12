import sys
sys.path.append('/Users/leelajosnakona/Leela/GitHub/US_Covid_vaccine_stats/lib/')
from functions import load_data, date_filter, sidebar_filters, county_map, county_rank, ageGender_chart, race_chart

import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt, os
import matplotlib.pyplot as plt
from vega_datasets import data
from datetime import date, timedelta


APP_TITLE = 'COVID-19 Vaccinations in the United States'
APP_SUB_TITLE = 'Source: COVID-19 Case Surveillance Public Use Data with Geography'


def main():

    ### Page Config
    st.set_page_config(page_title=APP_TITLE, page_icon=":mask", layout="wide")
    st.title(f":microbe: {APP_TITLE} :mask:")
    st.caption(APP_SUB_TITLE)
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

    ### Load Data
    df = load_data()
    df = df.dropna(subset=['res_state', 'res_county'])
    df = df.reset_index(drop=True)



    # dfg = df[df["age_group"].str.contains("Other")]
    # st.write(dfg)
    st.write(df.shape)

    #Display Filters and Map
    df, date1, date2 = date_filter(df)
    filtered_df, state, county = sidebar_filters(df)

    # st.write(filtered_df.head())
    # st.write(filtered_df.shape)


    # race = st.sidebar.multiselect("Pick your Race", df["race"].unique())
    # ethnicity = st.sidebar.multiselect("Pick your Ethnicity", df["ethnicity"].unique())

    # stateCounty_count = filtered_df.groupby(['res_state', 'state_fips_code', 'res_county', 'county_fips_code'])['res_county'].count().reset_index(name='count')
    stateCounty_count = filtered_df.groupby(['res_state', 'state_fips_code', 'res_county', 'county_fips_code'])['count'].sum().reset_index(name='Total')
    state_count = filtered_df.groupby(['res_state', 'state_fips_code'])['count'].sum().reset_index(name='Total')

    # st.write(stateCounty_count.head())
    # st.write(stateCounty_count.shape)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f" COVID-19 Vaccinations by County ")
        county_map(stateCounty_count, state_count)
        

    with col2:
        st.subheader(f" Top Ranked States ")
        county_rank(stateCounty_count)

    # filtered_df2 = filtered_df.fillna('Other')
    # AgeGender_count = filtered_df2.groupby(['res_state', 'res_county','case_month', 'age_group', 'gender'])['count'].sum().reset_index(name='Total')
    # race_ethnicity_ct = filtered_df2.groupby(['res_state', 'res_county','case_month','race','ethnicity'])['count'].sum().reset_index(name='Total')
    
    # # st.write(AgeGender_count.head())
    # st.write(stateCounty_count.shape)

    # col1, col2 = st.columns(2)

    # with col1:
    #     st.subheader(f"Vaccination status of {state} by Age Group by gender")
    #     ageGender_chart(AgeGender_count)

    # with col2:
    #     st.subheader("Vaccination status by Race by Ethnicity")
    #     race_chart(race_ethnicity_ct)

    ### session_state

    st.session_state['my_df'] = filtered_df
    st.session_state["my_date1"] = date1
    st.session_state["my_date2"] = date2
    st.session_state["my_state"] = state
    st.session_state["my_county"] = county
    st.write(st.session_state["my_df"])

    "st.session_state object:", st.session_state

if __name__ == "__main__":
    main()