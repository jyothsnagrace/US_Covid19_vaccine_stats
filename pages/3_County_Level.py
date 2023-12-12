
from lib.functions import load_data, date_filter, sidebar_filters, ethnicity_chart, ageGender_chart, race_chart, sidebar_filters2, session_assign, page_config

import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt, os
import matplotlib.pyplot as plt
from vega_datasets import data
from datetime import date, timedelta


def main():

    ### Page Config
    page_config()


    ### Load Data
    df = load_data()
    
    
    st.write("Dataset Dimensionality (Shape): ", df.shape)

    #Display Filters and Map
    df, date1, date2 = date_filter(df)
    filtered_df, state, county = sidebar_filters2(df)


    filtered_df2 = filtered_df.fillna('Other')
    AgeGender_count = filtered_df2.groupby(['res_state', 'res_county','case_month', 'age_group', 'gender'])['count'].sum().reset_index(name='Total')
    race_ct = filtered_df2.groupby(['res_state', 'res_county','case_month','race'])['count'].sum().reset_index(name='Total')
    ethnicity_ct = filtered_df2.groupby(['res_state', 'res_county','case_month','ethnicity'])['count'].sum().reset_index(name='Total')

    display_df = filtered_df2.groupby(['res_state', 'res_county','case_month', 'age_group', 'gender', 'race', 'ethnicity'])['count'].sum().reset_index(name='Total')

    # st.write(display_df)
    # st.write(stateCounty_count.shape)

    tab1, tab2, tab3 = st.tabs(["Violin Plot", "Bump Chart", "Pie Chart"])

    with tab1:
        st.subheader(f"Violin Plot by Age and Gender")
        ageGender_chart(AgeGender_count)

    with tab2:
        st.subheader("Bump Chart by Race over Time")
        race_chart(race_ct)

    with tab3:
        st.subheader("Pie Chart by ethnicity")
        ethnicity_chart(ethnicity_ct)

    ### session_state

    session_assign(filtered_df, date1, date2, state, county)

    # "st.session_state object:", st.session_state
    
    tab1, tab2 = st.tabs(["Session State filters", "Session df"])
    with tab1:
        st.write("Start Date: ", st.session_state["my_date1"]) 
        st.write("End Date: ", st.session_state["my_date2"]) 
        st.write("State : ", st.session_state["my_state"]) 
        st.write("County: ", st.session_state["my_county"]) 
    with tab2:
        st.write("df: ", st.session_state["my_df"]) 



if __name__ == "__main__":
    main()