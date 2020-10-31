import streamlit as st
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts

st.title('Child Opportunity Index')

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

# Select State
st.subheader('Statistics by State')
list_states = list(data['stateusps'].unique())
state = st.selectbox('Select State:', (list_states))

# Filter data
data = data[data['stateusps']==state]
data_10 = data[data['year']==2010]
data_15 = data[data['year']==2015]

b = (
    Bar()
    .add_xaxis(["Native American", "Asian", "Black", "Hispanic", "Other", "White", "Non-White"])
    .add_yaxis(
        "2010", [str(round(data_10['aian'].sum()/data_10['pop'].sum()*100, 2)),
                str(round(data_10['api'].sum()/data_10['pop'].sum()*100, 2)),
                str(round(data_10['black'].sum()/data_10['pop'].sum()*100, 2)),
                str(round(data_10['hisp'].sum()/data_10['pop'].sum()*100, 2)),
                str(round(data_10['other2'].sum()/data_10['pop'].sum()*100, 2)),
                str(round(data_10['white'].sum()/data_10['pop'].sum()*100, 2)),
                str(round(data_10['nonwhite'].sum()/data_10['pop'].sum()*100, 2))
               ]
    )
    .add_yaxis(
        "2015", [str(round(data_15['aian'].sum()/data_15['pop'].sum()*100, 2)),
                str(round(data_15['api'].sum()/data_15['pop'].sum()*100, 2)),
                str(round(data_15['black'].sum()/data_15['pop'].sum()*100, 2)),
                str(round(data_15['hisp'].sum()/data_15['pop'].sum()*100, 2)),
                str(round(data_15['other2'].sum()/data_15['pop'].sum()*100, 2)),
                str(round(data_15['white'].sum()/data_15['pop'].sum()*100, 2)),
                str(round(data_15['nonwhite'].sum()/data_15['pop'].sum()*100, 2))
               ]
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="State Population by Race", 
            subtitle="Number of children aged 0-17. Source: 5-Year American Community Survey Summary Files."
        ),
        #toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(b)

st.subheader('Filter by County')
list_counties = list(data['countyfips'].unique())
county = st.selectbox('Select County FIP Code:', (list_counties))

c_data_10 = data_10[data_10['countyfips']==county]
c_data_15 = data_15[data_15['countyfips']==county]

c = (
    Bar()
    .add_xaxis(["Native American", "Asian", "Black", "Hispanic", "Other", "White", "Non-White"])
    .add_yaxis(
        "2010", [str(round(c_data_10['aian'].sum()/c_data_10['pop'].sum()*100, 2)),
                str(round(c_data_10['api'].sum()/c_data_10['pop'].sum()*100, 2)),
                str(round(c_data_10['black'].sum()/c_data_10['pop'].sum()*100, 2)),
                str(round(c_data_10['hisp'].sum()/c_data_10['pop'].sum()*100, 2)),
                str(round(c_data_10['other2'].sum()/c_data_10['pop'].sum()*100, 2)),
                str(round(c_data_10['white'].sum()/c_data_10['pop'].sum()*100, 2)),
                str(round(c_data_10['nonwhite'].sum()/c_data_10['pop'].sum()*100, 2))
               ]
    )
    .add_yaxis(
        "2015", [str(round(c_data_15['aian'].sum()/c_data_15['pop'].sum()*100, 2)),
                str(round(c_data_15['api'].sum()/c_data_15['pop'].sum()*100, 2)),
                str(round(c_data_15['black'].sum()/c_data_15['pop'].sum()*100, 2)),
                str(round(c_data_15['hisp'].sum()/c_data_15['pop'].sum()*100, 2)),
                str(round(c_data_15['other2'].sum()/c_data_15['pop'].sum()*100, 2)),
                str(round(c_data_15['white'].sum()/c_data_15['pop'].sum()*100, 2)),
                str(round(c_data_15['nonwhite'].sum()/c_data_15['pop'].sum()*100, 2))
               ]
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="County Population by Race", 
            subtitle="Number of children aged 0-17. Source: 5-Year American Community Survey Summary Files."
        ),
        #toolbox_opts=opts.ToolboxOpts(),
    )
)
st_pyecharts(c)
