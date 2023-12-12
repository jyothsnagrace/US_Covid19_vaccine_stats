import sys
sys.path.append('/Users/leelajosnakona/Leela/GitHub/US_Covid_vaccine_stats/lib/')
from functions import load_data, date_filter, sidebar_filters, ethnicity_chart, ageGender_chart, race_chart, sidebar_filters2

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

    
    # "st.session_state object:", st.session_state


    ### Load Data
    df = load_data()
    df, date1, date2 = date_filter(df)
    
    # if 'my_df' in st.session_state:
    #     filtered_df =  st.session_state['my_df']  

    
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

    st.session_state['my_df'] = filtered_df
    st.session_state["my_date1"] = date1
    st.session_state["my_date2"] = date2
    
    # st.write(st.session_state["my_df"])

if __name__ == "__main__":
    main()