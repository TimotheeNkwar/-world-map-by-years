import plotly.graph_objects as go
from plotly.offline import iplot
import pandas as pd
import streamlit as st
popu = pd.read_csv("world_population.csv")

popu.rename(columns={"Country/Territory":"Country","CCA3":"Code"},inplace=True)
popu.head()

st.title("World Population By Years")


popu['Country_Capital'] = popu['Country'] + ' - ' + popu['Capital']+ ' - ' + popu['Continent']
popu['Combined_Z'] = popu['1970 Population'] + popu['World Population Percentage']
#natural earth,conic equal area,azimuthal equal area,orthographic,mercator
data_1970 = dict(
    type='choropleth',
    locations=popu['Code'],
    colorscale="Magma_r",
    z=popu['1970 Population'],
    text=popu['Country_Capital'],
    colorbar={'title': '1970 Population'},
    autocolorscale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    showscale=True,
    name='1970'
)

data_1980 = dict(
    type='choropleth',
    locations=popu['Code'],
    colorscale="Magma_r",
    z=popu['1980 Population'],
    text=popu['Country_Capital'],
    colorbar={'title': '1980 Population'},
    autocolorscale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    showscale=True,
    name='1980'
)

data_1990 = dict(
    type='choropleth',
    locations=popu['Code'],
    colorscale="Magma_r",
    z=popu['1990 Population'],
    text=popu['Country_Capital'],
    colorbar={'title': '1990 Population'},
    autocolorscale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    showscale=True,
    name='1990'
)

data_2000 = dict(
    type='choropleth',
    locations=popu['Code'],
    colorscale="Magma_r",
    z=popu['2000 Population'],
    text=popu['Country_Capital'],
    colorbar={'title': '2000 Population'},
    autocolorscale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    showscale=True,
    name='2000'
)

data_2010 = dict(
    type='choropleth',
    locations=popu['Code'],
    colorscale="Magma_r",
    z=popu['2010 Population'],
    text=popu['Country_Capital'],
    colorbar={'title': '2010 Population'},
    autocolorscale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    showscale=True,
    name='2010'
)

data_2015 = dict(
    type='choropleth',
    locations=popu['Code'],
    colorscale="Magma_r",
    z=popu['2015 Population'],
    text=popu['Country_Capital'],
    colorbar={'title': '2015 Population'},
    autocolorscale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    showscale=True,
    name='2015'
)

data_2020 = dict(
    type='choropleth',
    locations=popu['Code'],
    colorscale="Magma_r",
    z=popu['2020 Population'],
    text=popu['Country_Capital'],
    colorbar={'title': '2020 Population'},
    autocolorscale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    showscale=True,
    name='2020'
)

data_2022 = dict(
    type='choropleth',
    locations=popu['Code'],
    colorscale="Magma_r",
    z=popu['2022 Population'],
    text=popu['Country_Capital'],
    colorbar={'title': '2022 Population'},
    autocolorscale=False,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    showscale=True,
    name='2022'
)

# Create initial figure with 1970 data
fig = go.Figure(data=[data_1970])

# Add other data traces
fig.add_trace(go.Choropleth(data_1980))
fig.add_trace(go.Choropleth(data_1990))
fig.add_trace(go.Choropleth(data_2000))
fig.add_trace(go.Choropleth(data_2010))
fig.add_trace(go.Choropleth(data_2015))
fig.add_trace(go.Choropleth(data_2020))
fig.add_trace(go.Choropleth(data_2022))

# Set visibility for each trace
for i in range(1, len(fig.data)):
    fig.data[i].visible = False

# Define the layout with buttons
fig.update_layout(

    title='Comparison of world population by year',
    geo=dict(
        showframe=True,
        projection=dict(type='orthographic'),
    ),
    width=1200,
    height=1000,
    updatemenus=[{
        'buttons': [
            {'label': '1970', 'method': 'update', 'args': [{'visible': [True] + [False]*7}, {'title': 'Population in 1970'}]},
            {'label': '1980', 'method': 'update', 'args': [{'visible': [False, True] + [False]*6}, {'title': 'Population in 1980'}]},
            {'label': '1990', 'method': 'update', 'args': [{'visible': [False]*2 + [True] + [False]*5}, {'title': 'Population in 1990'}]},
            {'label': '2000', 'method': 'update', 'args': [{'visible': [False]*3 + [True] + [False]*4}, {'title': 'Population in 2000'}]},
            {'label': '2010', 'method': 'update', 'args': [{'visible': [False]*4 + [True] + [False]*3}, {'title': 'Population in 2010'}]},
            {'label': '2015', 'method': 'update', 'args': [{'visible': [False]*5 + [True] + [False]*2}, {'title': 'Population in 2015'}]},
            {'label': '2020', 'method': 'update', 'args': [{'visible': [False]*6 + [True] + [False]}, {'title': 'Population in 2020'}]},
            {'label': '2022', 'method': 'update', 'args': [{'visible': [False]*7 + [True]}, {'title': 'Population in 2022'}]},
        ],
        'direction': 'right',
        'showactive': True,
    }]
)

# Display the map
st.plotly_chart(fig, use_container_width=True)
