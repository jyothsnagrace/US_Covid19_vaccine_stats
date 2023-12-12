
# US COVID-19 Vaccination Statistics
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://uscovidvaccine-stats.streamlit.app)


## Author

Leela Josna Kona 
- [Tableau Public Profile](https://public.tableau.com/app/profile/lkona)
- [LinkedIn](https://www.linkedin.com/in/lkona/)


Interactive Dashboard of COVID-19 infections and vaccinations employing [Streamlit](https://www.streamlit.io) module .
You can try [here](https://uscovidvaccine-stats.streamlit.app/).

## Primary objectives
* Basic options for users to choose
  * Cumulative or daily changes measures
  * Global aggregate stat or per-country information
* Display a basic statistics for selected area (Global or for specific country)
* Draw a heatmap detailing given a region and measure (e.g., Daily confirmed patients increases in the US)
* Draw a Choropleth with the same selection (Country-level or state-level comparisons)



## Data sources and helpful resources
* Vaccinations data source
  * [Johns Hopkins University GoVex GitHub](https://github.com/govex/COVID-19): Global nCov-19 vaccinations (+ infections) dataset
* Geographic data 
  * [NaturalEarth](http://naturalearthdata.com/): Geographical shapedata for countries (admin0) and states-level (admin1) data to be used (1:10m data is used for selected countries for states details while 1:50m used for others)

## Descriptions of objects
* Heatmap
  * Two separate charts are drawn (Infections: confirmed, casualties / Vaccinations: administered, fully vaccinated)
  * Regions on y-axis are pre-sorted by the figures (ordered in a descending manner for top-25 disricts)
* Barplot (Vaccinations-only)
  * For countries which don't provide province/state-level data, single stacked barplot with both measures are drawn (administered and fully vaccinated)
* Choropleth
  * Two measures are drawn on a single choropleth (Color depths: confirmed / administered, Elevations: casualties / fully vaccinated)
  * One measure is shown by the color depth while the other is represented by elevations of the regions
  
## Selected modules used
  * [Altair](http://altair-viz.github.io/): Altair chart module used to draw heatmap (`streamlit.altair_chart`)
  * [Pydeck](http://pydeck.gl/): Pydeck mapping module used to draw Choropleth/PolygonLayer (`streamlit.pydeck_chart`)


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

