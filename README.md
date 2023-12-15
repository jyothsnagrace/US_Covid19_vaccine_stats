
# US COVID-19 Vaccination Statistics
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://uscovid19vaccine-stats.streamlit.app/){:target="_blank"}

An Interactive Streamlit App Dashboard to visualize and analyze USA Covid-19 Vaccination stats [Streamlit](https://www.streamlit.io) module. You can try [here](https://uscovid19vaccine-stats.streamlit.app/).  

Data from the Centers for Disease Control and Prevention (CDC) collected during Jan 2020 to Dec 2022, were analyzed to assess COVID-19 vaccination, intent for vaccination, and attitudes towards vaccination among sociodemographic categories like Gender, Age group, race and ethnicity across USA at county level.

## Results:
At anytime Covid 19 Vaccination coverage was highest in women aged 18–49 years. Men had lower coverage than women in all age groups. 
Intent to definitely get a COVID-19 vaccine was high in non-Hispanic/Laino and Native Hawaiian and other Pacific Island (NH/OPI). While, whites have higher levels of vaccine hesitancy.

## Author

Leela Josna Kona
- [LinkedIn](https://www.linkedin.com/in/lkona/)

## Primary objectives
* Basic options for users to choose
  * Dataset Date Period
  * US State and County Multiselect Filters
  * Maintaining and updating filter values across multiple pages with session state
  * A Home page and Multipage app to categorize the dataset at different hierarchy
     * US State Reports:
       * Display a COVID-19 Vaccination Coverage Across U.S. Counties in a Geoshape Map
       * Draw a Rank Chart with the selection (state-level or County-level comparisons)
     * Detail Reports and North Carolina - level Reports:
       * Draw a Violin Plot of Total Vaccination Distribution accross Age and Gender
       * Draw a line chart of Weekly Initiation by Age group in [State], [County]
       * Draw a Bump Chart by Race over Time in [State], [County]
       * Draw a Pie Chart by Ethnicity Breakdown for the selected date range

## Data sources and design
* Vaccinations data source
  * [Centers for Disease Control and Prevention (CDC)](https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4/about_data): COVID-19 Case Surveillance Public Use Data with Geography dataset
* Geographic data
  * [Altair Vega_Datasets]([http://naturalearthdata.com/](https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/us-10m.json#)): Geographical shapedata for states and counties
  * counties <- alt$topo_feature(vega_data$us_10m$url, "counties")
  * states <- alt$topo_feature(vega_data$us_10m$url, "states")

    
## Selected modules used
  * [Streamlit](https://www.streamlit.io)
  * [Altair](http://altair-viz.github.io/): Altair chart module used to draw Geoshape Map and other charts like Bump, Pie, Rank  (`streamlit.altair_chart`)
  * [Plotly](https://plotly.com/): Plotly chart module used to draw Violin Plot, (`streamlit.plotly_chart`)
  * [Multipage app](https://docs.streamlit.io/library/get-started/multipage-apps)
  * [Session State](https://docs.streamlit.io/library/api-reference/session-state)


## Snapshots
### 1. Landing Page
![Home](https://github.com/jyothsnagrace/US_Covid19_vaccine_stats/blob/main/images/1.%20Home%20Screen.png))

### 2. US State Report
![US State Report](https://github.com/jyothsnagrace/US_Covid19_vaccine_stats/blob/main/images/2b.%20US%20State%20report.png)

 #### Input values saved in Session state
 ![Session State](https://github.com/jyothsnagrace/US_Covid19_vaccine_stats/blob/main/images/2a.%20Capturing%20Session%20State%20Values.png)

 #### US State Report - selected states
 ![US State Report](https://github.com/jyothsnagrace/US_Covid19_vaccine_stats/blob/main/images/2c.%20US%20State%20report.png)

 #### US State Report - selected county
 ![US State Report](https://github.com/jyothsnagrace/US_Covid19_vaccine_stats/blob/main/images/2b.%20US%20State%20report-2.png)

### 3. Detail Reports
 #### Vaccinations - Age and Gender Distribution
 ![Age and Gender Distribution](https://github.com/jyothsnagrace/US_Covid19_vaccine_stats/blob/main/images/3a.%20Age%20and%20Gender%20Distribution.png)
 
  #### Vaccinations - Age Group Trend
 ![Age and Gender Distribution](https://github.com/jyothsnagrace/US_Covid19_vaccine_stats/blob/main/images/3b.%20Age%20Group%20Trend.png)

  #### Vaccinations - Race Dynamics
 ![Race Dynamics](https://github.com/jyothsnagrace/US_Covid19_vaccine_stats/blob/main/images/3c.%20Race%20Dynamics.png)

  #### Vaccinations - Ethnicity Breakdown
 ![Ethnicity Breakdown](https://github.com/jyothsnagrace/US_Covid19_vaccine_stats/blob/main/images/3d.%20Ethnicity%20Breakdown.png)


## Future work
This Framework can be used at global scale and can include additional virus vaccination data. Adding more criteria in Visualizations can provide understanding of vaccination dynamics.
This promotes an equitable vaccine distribution and reduces racial and ethnic disparities in vaccination.
Also, work on the session state capturing sidebar input values across multiple pages.
