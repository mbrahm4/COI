import streamlit as st
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
import plotly.figure_factory as ff
import plotly.express as px

st.sidebar.title("Navigation")
nav = st.sidebar.selectbox('Go to:', ('Home Page', 
                                      'Population Statistics',
                                      'Child Opportunity Index'))

st.title('Child Opportunity Index')

if nav == 'Home Page':
    st.markdown("Neighborhoods matter for children's health and development. All children should live in neighbordhoods with access to good schools, healthy foods, safe parks and playgrounds, clean air, safe housing and living-wage jobs for the adults in their lives. However, far too many children live in neighborhoods that lack these conditions.")

    st.subheader("What is the Child Opportunity Index?")
    st.info("The Child Opportunity Index (COI) measures neighborhood opportunity along three domains that matter for children: 1) Education, 2) Health and Environment, and 3) Social and Economic.")

    st.markdown("The COI ranks neighborhood opportunity based on 29 common conditions within these domains. Each neighborhood receives a Child Opportunity Score and is assigned to an opportunity level: very low, low, moderate, high, or very high opportunity.")

    st.subheader("Data Source:")
    st.markdown("[DiversityDataKids.org](http://www.diversitydatakids.org/child-opportunity-index)")


elif nav == 'Population Statistics':

    DATA_URL = ('http://data.diversitydatakids.org/datastore/dump/44ee1ea6-a3df-4af3-93b7-c4695d5ab6a6?bom=True')

    @st.cache
    def load_data():
        data = pd.read_csv(DATA_URL)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        return data

    # Load Data
    data_load_state = st.text('Loading data...')
    data = load_data()
    data_load_state.text('Loading data...done!')

    st.sidebar.markdown("Neighborhoods matter for children's health and development. All children should live in neighbordhoods with access to good schools, healthy foods, safe parks and playgrounds, clean air, safe housing and living-wage jobs for the adults in their lives. However, far too many children live in neighborhoods that lack these conditions.")

    st.sidebar.subheader("What is the Child Opportunity Index?")
    st.sidebar.info("The Child Opportunity Index (COI) measures neighborhood opportunity along three domains that matter for children: 1) Education, 2) Health and Environment, and 3) Social and Economic.")

    st.sidebar.markdown("The COI ranks neighborhood opportunity based on 29 common conditions within these domains. Each neighborhood receives a Child Opportunity Score and is assigned to an opportunity level: very low, low, moderate, high, or very high opportunity.")

    st.sidebar.subheader("Data Source:")
    st.sidebar.markdown("[DiversityDataKids.org](http://www.diversitydatakids.org/child-opportunity-index)")

    # Select State
    st.subheader('Population by State')
    list_states = list(data['stateusps'].unique())
    state = st.selectbox('Select State:', (list_states))
    
    # Select Year
    list_years = list(data['year'].unique())
    year = st.selectbox('Select Year:', (list_years))
    
    # Filter data
    data = data[data['stateusps']==state]
    data = data[data['year']==year]
    
    st.write("Total Population in " + state + ": ", data['pop'].sum()) 
    
    values = [data['aian'].sum(),
              data['api'].sum(),
              data['black'].sum(),
              data['hisp'].sum(),
              data['other2'].sum(),
              data['nonwhite'].sum(),
              data['white'].sum()
             ]
    names = ['Native American', 
             'Asian', 
             'Black', 
             'Hispanic', 
             'Other', 
             'Non-White', 
             'White']

    fig = px.pie(data, 
                 values=values, 
                 names=names, 
                 color_discrete_sequence=px.colors.sequential.Blugrn, 
                 hole=.6)
    
    st.plotly_chart(fig)

    st.subheader('Population by County')
        
    races = ['aian', 'api', 'black', 'hisp', 'other2', 'nonwhite', 'white']
    race = st.selectbox('Select Population:', (races))
    county_race = data.groupby(['countyfips'])[races].agg('sum').reset_index()
    
    fips = list(county_race.countyfips)
    values = county_race[race]
    
    fig = ff.create_choropleth(fips=fips, 
                               values=values, 
                               scope=[state],
                               county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
                               legend_title='Population by County'
                               )
    fig.layout.template = None
    st.plotly_chart(fig)
        
    # Filter by County
    select_county = list(data['countyfips'].unique())
    county = st.selectbox('Select County:', (select_county))
    
    # Filter data
    data = data[data['countyfips']==county]
    
    st.write("Total Population in ", str(county), ": ", data['pop'].sum()) 
    
    
    values = [data['aian'].sum(),
              data['api'].sum(),
              data['black'].sum(),
              data['hisp'].sum(),
              data['other2'].sum(),
              data['nonwhite'].sum(),
              data['white'].sum()
             ]
    names = ['Native American', 
             'Asian', 
             'Black', 
             'Hispanic', 
             'Other', 
             'Non-White', 
             'White']

    fig = px.pie(data, 
                 values=values, 
                 names=names, 
                 color_discrete_sequence=px.colors.sequential.Blugrn, 
                 hole=.6)
    
    st.plotly_chart(fig)



elif nav == 'Child Opportunity Index':
    
    st.subheader('Explore COI by Neighborhood')
    
    DATA_URL = ('http://data.diversitydatakids.org/datastore/dump/080cfe52-90aa-4925-beaa-90efb04ab7fb?bom=True')

    @st.cache
    def load_data():
        data = pd.read_csv(DATA_URL)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        return data

    # Load Data
    data_load_state = st.text('Loading data...')
    data = load_data()
    data_load_state.text('Loading data...done!')
    
    st.sidebar.info("The Child Opportunity Index (COI) 2.0, is a tool that describes and quantifies the neighborhood conditions U.S. children experience today, ranking them from lowest to highest opportunity.")
    
    st.sidebar.markdown("Neighborhoods matter for children's health and development. All children should live in neighbordhoods with access to good schools, healthy foods, safe parks and playgrounds, clean air, safe housing and living-wage jobs for the adults in their lives. However, far too many children, in particular, African American, Hispanic and Native American children live in neighborhoods that lack these conditions.")

    st.sidebar.markdown("The COI measures neighborhood opportunity along three domains that matter for children: 1) Education, 2) Health and Environment, and 3) Social and Economic. The COI ranks neighborhood opportunity based on 29 common conditions within these domains. Each neighborhood receives a Child Opportunity Score and is assigned to an opportunity level: very low, low, moderate, high, or very high opportunity.")

    st.sidebar.subheader("Data Source:")
    st.sidebar.markdown("The COI 2.0 is funded by the Robert Wood Johnson Foundation and the W.K. Kellogg Foundation. More information available at [DiversityDataKids.org](http://www.diversitydatakids.org/child-opportunity-index)")
    
    # Select State
    st.subheader('Statistics by State')
    
    st.write("The map below shows the average State-normed Child Opportunity Scores (from 1 to 100) for the overall COI for each county. Note that, the COI score for each GEOID within a county is averaged.")
    
    list_states = list(data['stateusps'].unique())
    state = st.selectbox('Select State:', (list_states))
    
    # Select Year
    list_years = list(data['year'].unique())
    year = st.selectbox('Select Year:', (list_years))
    
    # Filter data
    data = data[data['stateusps']==state]
    data = data[data['year']==year]
    
    map_d = data.groupby(['countyfips'])['r_coi_stt'].agg('mean').reset_index()
    
    fips = list(map_d.countyfips)
    values = map_d["r_coi_stt"]
    
    fig = ff.create_choropleth(fips=fips, 
                               values=values, 
                               scope=[state],
                               binning_endpoints=[20, 40, 60, 80, 100],
                               county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
                               legend_title='COI by County'
                               )
    fig.layout.template = None
    st.plotly_chart(fig)
    
    # Select County
    st.subheader('Filter by County')
    list_counties = list(data['countyfips'].unique())
    county = st.selectbox('Select County FIP Code:', (list_counties))
    
    
    data = data[data['countyfips']==county]
    st.write(data)
    
   
    
