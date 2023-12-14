
from lib.functions import load_data, date_filter, sidebar_filters, ethnicity_chart, ageGender_chart, race_chart, sidebar_filters2, session_assign, page_config, agePeriod_chart

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

    with open('lib/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    ### Load Data
    df = load_data()
    
    
    st.write("Dataset Shape: ", df.shape)

    #Display Filters and Map
    df, date1, date2 = date_filter(df)
    filtered_df, state, county = sidebar_filters2(df)


    filtered_df2 = filtered_df.fillna('Other')
    AgeGender_count = filtered_df2.groupby(['res_state', 'res_county','case_month', 'age_group', 'gender'])['count'].sum().reset_index(name='Total')
    race_ct = filtered_df2.groupby(['res_state', 'res_county','case_month','race'])['count'].sum().reset_index(name='Total')
    ethnicity_ct = filtered_df2.groupby(['res_state', 'res_county','case_month','ethnicity'])['count'].sum().reset_index(name='Total')
    AgeGroup_count = AgeGender_count.groupby(['case_month','age_group'])['Total'].sum().reset_index(name='Total')

    race_ct1 = race_ct.groupby(['case_month','race'])['Total'].sum().reset_index(name='Total')
    ethnicity_ct1 = ethnicity_ct.groupby(['ethnicity'])['Total'].sum().reset_index(name='Total')


    display_df = filtered_df2.groupby(['res_state', 'res_county','case_month', 'age_group', 'gender', 'race', 'ethnicity'])['count'].sum().reset_index(name='Total')

    d1 = date1.strftime("%b %Y")

    d2 = date2.strftime("%b %Y")

    statec = ','.join(state)
    countyc = ','.join(county)

    if state:
        chart_tag = statec + ', ' + countyc
    else:
        chart_tag = 'USA'

    tab1, tab2, tab3, tab4 = st.tabs(["Age and Gender Distribution", "Weekly Initiation by Age Group", "Race Dynamics", "Ethnicity Breakdown"])
    
 

    with tab1:
        st.subheader(f"Age and Gender Distribution from {d1} to {d2}")
        caption =""":gray[**NC State Results:** Vaccination coverage was highest in women aged 18–49 years.  
        Men had lower coverage than women in all age groups.]"""
        st.markdown(caption)
        ageGender_chart(AgeGender_count)

    with tab2:
        st.subheader(f"Weekly Initiation by Age group in {chart_tag}")
        st.caption(f"**NC State Results:** Vaccination coverage was highest for age group 18–49 years.")
        agePeriod_chart(AgeGroup_count)

    with tab3:
        st.subheader(f"Race Dynamics Over Time in {chart_tag}")
        caption =""":gray[**NC State Results:** Intent to definitely get a COVID-19 vaccine was high in American Indian or Alaska Native (AI/AN).  
        Whites have higher levels of vaccine hesitancy.]"""
        st.markdown(caption)
        race_chart(race_ct1)

    with tab4:
        st.subheader(f"Ethnicity Breakdown from {d1} to {d2}")
        st.caption(f"**NC State Results:** Vaccination coverage was highest for non-Hispanic/Laino.")
        ethnicity_chart(ethnicity_ct1)

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
