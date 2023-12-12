
# US COVID-19 Vaccination Statistics
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://uscovid19vaccine-stats.streamlit.app/)

An Interactive Streamlit App Dashboard to visualize and analyze USA Covid-19 Vaccination stats [Streamlit](https://www.streamlit.io) module .
You can try [here](https://uscovid19vaccine-stats.streamlit.app/).

## Author

Leela Josna Kona
- [LinkedIn](https://www.linkedin.com/in/lkona/)

## Primary objectives
* Basic options for users to choose
  * Dataset Date Period
  * US State and County Multiselect Filters
  * Reads and updates Filter values usng Session State
  * A Home page and Multipage app to categorize the dataset at different hierarchy
     * US State Reports:
       * Display a Covid 19 Vaccination statistics for selected area (US or for specific State or County)
       * Draw a Rank Chart with the same selection (state-level or County-level comparisons)
     * NC Reports:
       * Draw a Violin Plot of Total Vaccination Count accross Age-Group and Gender
       * Draw a Bump Chart by Race over Time
       * Draw a Pie Chart by Ethnicity

## Data sources and helpful resources
* Vaccinations data source
  * [Centers for Disease Control and Prevention (CDC)](https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4/about_data): COVID-19 Case Surveillance Public Use Data with Geography dataset
* Geographic data
  * [Altair Vega_Datasets]([http://naturalearthdata.com/](https://cdn.jsdelivr.net/npm/vega-datasets@v1.29.0/data/us-10m.json#)): Geographical shapedata for states and counties
  * counties <- alt$topo_feature(vega_data$us_10m$url, "counties")
  * states <- alt$topo_feature(vega_data$us_10m$url, "states")

## Descriptions of objects
* Geoshape Map
  * US states and counties map are drawn (Total number of vaccinated)
* Top Ranked Barplot
  * States on y-axis are pre-sorted by the Total vaccinated and displayed counties as stacked
* Violin Plot
  * For North Carolina State and its selected counties by Age-Group and Gender
* Bump Chart
  * For North Carolina State and its selected counties by Race over Time
* Pie
  * For North Carolina State and its selected counties by Ethnicity
    
## Selected modules used
  * [Streamlit](https://www.streamlit.io)
  * [Altair](http://altair-viz.github.io/): Altair chart module used to draw Geoshape Map and other charts like Bump, Pie, Rank  (`streamlit.altair_chart`)
  * [Plotly](https://plotly.com/): Plotly chart module used to draw Violin Plot, (`streamlit.plotly_chart`)
  * [Multipage app](https://docs.streamlit.io/library/get-started/multipage-apps)
  * [Session State](https://docs.streamlit.io/library/api-reference/session-state)


## Snapshots
### Main Landing Page
![main](https://github.com/staedi/Streamlit_nCov19/raw/master/samples/main_v2.png)

### Heatmap - Infections
![infections_heatmap](https://github.com/staedi/Streamlit_nCov19/raw/master/samples/heatmap_infections.png)

### Heatmap - Vaccinations
![vaccinations_heatmap](https://github.com/staedi/Streamlit_nCov19/raw/master/samples/heatmap_vaccinations.png)

### Barplot - Vaccinations (Country-level)
![barplot](https://github.com/staedi/Streamlit_nCov19/raw/master/samples/stackedbar_vaccinations.png)

### Choropleth - Infections
![infections_choropleth](https://github.com/staedi/Streamlit_nCov19/raw/master/samples/choropleth_infections.png)

### Choropleth - Vaccinations
![vaccinations_choropleth](https://github.com/staedi/Streamlit_nCov19/raw/master/samples/choropleth_vaccinations.png)

