from dash import dcc, html, callback, Input, Output

import dash

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

dash.register_page(
    __name__,
    title='Civilian Targeting | Dashboard',
    order=2
)

########################################### Processing #############################################
df = pd.read_excel(r'data/palestine_hrp_civilian_targeting_events_and_fatalities_by_month-year_as-of-17apr2024.xlsx',sheet_name='Data')
total_fatalities = df['Fatalities'].sum()
total_events = df['Events'].sum()

months = ['January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December']

########################################### Graphs #################################################
def filter_df(df, value):
    if value == 'Gaza Strip':
        tmp = df[df['Admin1']==value]
    elif value == 'West Bank':
        tmp = df[df['Admin1']==value]
    elif value == '7 Oct':
        df = df[(df['Year'] == 2023)]
    else:
        tmp = df
    return tmp

def pieEvents(df):
    admin1_sum = df.groupby('Admin1')['Events'].sum().reset_index()
    fig = px.pie(admin1_sum, values='Events', names='Admin1',
                title='Events Distributions',
                # color_discrete_sequence=['#ff553b', 'blue'],
                template='plotly_white')
    
    fig.update_layout(
        title_x=0.5,
        plot_bgcolor='rgba(0, 0, 0, .53)',
        paper_bgcolor='rgba(0, 0, 0, .53)',
        # margin=dict(l=50, r=50, t=50, b=50),
        font=dict(color='white')
    )
    #fig.layout.margin = dict(l=40, r=30, t=50, b=40)
    return fig


def pieFatalities(df):
    admin1_sum = df.groupby('Admin1')['Fatalities'].sum().reset_index()
    fig = px.pie(admin1_sum, values='Fatalities', names='Admin1',
                title='Fatalities Distribution',
                color_discrete_sequence=['#ef553b', '#636efa'],
                template='plotly_white')
    
    # order of legend is reversed 
    fig.update_layout(legend_traceorder="reversed"),
    fig.update_layout(title_x=0.5),
    fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0.53)',
            'paper_bgcolor': 'rgba(0,0,0,0.53)'
        },
        # margin=dict(l=50, r=50, t=50, b=50),
        font = dict(color = 'white'),)
    
    return fig 


def bar3(df, value):
    tmp = filter_df(df, value)

    tmp_sum = tmp.groupby('Admin2')[['Events','Fatalities']].sum().reset_index()
    fig = px.bar(tmp_sum, x='Admin2', y='Fatalities',
                labels={'Admin2': 'City', 'Fatalities': 'Fatalities'},
                title=f'Sum of Fatalities in {value}',
                template='plotly_white')
    
    # Rotate x-axis labels for better readability
    fig.update_layout(title_x=0.5),
    fig.update_layout(xaxis_tickangle=-45,
                    plot_bgcolor='rgba(0, 0, 0, 0)',
                    paper_bgcolor='rgba(0, 0, 0, 0.53)',
                    font = dict(color = 'white'),
                    legend=dict(x=0, y=1, bgcolor='rgba(255, 255, 255, 0.5)')  
    )

    return fig

def bar4(df, value):
    tmp = filter_df(df, value)

    tmp_sum = tmp.groupby('Admin2')[['Events','Fatalities']].sum().reset_index()
    fig = px.bar(tmp_sum, x='Admin2', y='Events',
                labels={'Admin2': 'City', 'Events': 'Events'},
                title=f'Sum of Events Caused in {value}',
                template='plotly_white')

    fig.update_layout(title_x=0.5,
                    xaxis_tickangle=-45,
                    plot_bgcolor='rgba(0, 0, 0, 0)',
                    paper_bgcolor='rgba(0, 0, 0, 0.53)',
                    font = dict(color = 'white'),
                    legend=dict(x=0, y=1, bgcolor='rgba(255, 255, 255, 0.5)')  
    )

    return fig


def lineMonthlyEvents(df, value):
    tmp = filter_df(df, value)

    tmp['Month'] = pd.Categorical(tmp['Month'], categories=months, ordered=True)
    monthly_data = tmp.groupby('Month', observed=False)['Events'].sum().reset_index()
    fig = px.line(monthly_data, x='Month', y=['Events'], markers=True,
                title=f'Total Monthly Events {value}')

    # Update layout for better visualization
    fig.update_layout(title_x=0.5,
        font = dict(color = 'white'),
        xaxis_title='Month',
        yaxis_title='Events Count',
        showlegend=False,

        plot_bgcolor='rgba(0, 0, 0, 0.53)',
        paper_bgcolor='rgba(0, 0, 0, 0.53)',
    )
    return fig

def lineMonthlyFatalities(df, value):
    tmp = filter_df(df, value)

    tmp['Month'] = pd.Categorical(tmp['Month'], categories=months, ordered=True)

    monthly_data = tmp.groupby('Month', observed=False)['Fatalities'].sum().reset_index()
    fig = px.line(monthly_data, x='Month', y=['Fatalities'], markers=True,
                title=f'Total Monthly Fatalities in {value}')

    # Update layout for better visualization
    fig.update_layout(title_x=0.5,
        font = dict(color = 'white'),
        xaxis_title='Month',
        yaxis_title='Fatalities Count',
        plot_bgcolor='rgba(0, 0, 0, 0.53)',
        paper_bgcolor='rgba(0, 0, 0, 0.53)',
        showlegend=False,
        # legend=dict(x=0, y=1, bgcolor='rgba(255, 255, 255, 0.5)')  # Place legend inside with white background

    )
    return fig

def tree(df):

    fig = px.treemap(df, path=['Admin1', 'Admin2'], values='Events',
                    title='Where most of civilian targeting ocuurs?',
                    color_continuous_scale='RdBu')
    fig.update_layout(title_x=0.5),
    
    fig.update_layout( 
        plot_bgcolor='rgba(0, 0, 0, .53)',
        paper_bgcolor='rgba(0, 0, 0, .53)',
        font = dict(color = 'white'))
    # fig.data[0].textinfo = 'label+text+value+current path'
    fig.data[0].textinfo = None
    # fig.layout.hovermode = True
    return fig

def map1(df):
        
    governorates = {
        'Gaza': [(31.5050311, 34.4641381), 5986], 
        'North Gaza': [(31.5501268, 34.5033134), 3393],
        'Khan Yunis': [(31.3457612, 34.3025277), 1652],
        'Rafah': [(31.2752047, 34.2558269), 1288],
        'Deir al-Balah': [(31.4183455, 34.3502476), 2105],
        
        'Nablus': [(32.2205316, 35.2569374), 14],
        'Jenin': [(32.4618837, 35.297566), 5],
        'Ramallah and al-Bira': [(31.9106212, 35.2088129), 4],
        'Hebron': [(31.5304303, 35.0879406), 8],
        'Tulkarm': [(32.3111468, 35.0275505), 12],
        'Bethlehem': [(31.7043556, 35.2061876), 0],
        'East Jerusalem': [(31.78336, 35.23388), 75],
        'al-Quds': [(31.8912806, 35.2003213), 55],
        'Gush Katif': [(31.42507, 34.3734), 25],
        'Qalqiliya': [(32.18966, 34.97063), 2],
        'Tubas': [(32.3234392, 35.3693661), 1],
        'Jericho': [(31.855991, 35.4598851), 1],
        'Salfit': [(32.0851611, 35.1815442), 0]
    }

    # Create lists to store data for scatter map
    lats = []
    lons = []
    text = []
    sizes = []

    # Populate lists with coordinates, text, and sizes based on fatalities
    fatalities = []
    for governorate, data in governorates.items():
        city_coordinates = data[0]
        fat = data[1]
        fatalities.append(fat)
        lats.append(city_coordinates[0])
        lons.append(city_coordinates[1])
        text.append(f" {governorate} - Fatalities = {fat}")
        # text.append(f"{city_coordinates[0]}, {city_coordinates[1]} - {governorate}")
        # Calculate size of marker based on fatalities (adjust scale factor as needed)
        sizes.append(fat * 0.0155)

    # Create a scattermapbox trace
    fig = go.Figure(go.Scattermapbox(
        lat=lats,
        lon=lons,
        mode='markers',
        # hovertext=fatalities,
        # hoverinfo='all',
        marker=go.scattermapbox.Marker(
            size=sizes,
            color='red',  # You can change the color of the circles here
            opacity=0.35,
        ),
        text=text,
    ))


    # Update layout for the map
    fig.update_layout(
        title='Fataliteies in Palastine scaled by radius',
        font = dict(color = 'white'),
        plot_bgcolor='rgba(0, 0, 0, .53)',
        paper_bgcolor='rgba(0, 0, 0, .53)',
        hovermode='closest',
        mapbox=dict(
            accesstoken='YOUR_MAPBOX_TOKEN',
            style='open-street-map',  # Change map style if needed
            bearing=0,
            center=dict(
                lat=31.90,
                lon=34.80
            ),
            pitch=0,
            zoom=6
        )

    )
    fig.update_layout(title_x=0.5),

    return fig


########################################### ####### #################################################


def addCardBody(title, value, image_src, style=None):
    return dbc.CardBody(
            [
                dmc.Container(
                    html.Img(src=image_src, className="card-img-top", 
                             height='200px', style={'fit': 'cover'}
                            ),
                ),
                dmc.Stack([
                    html.H4(value, className="ban"),
                    html.H4(title, className="ban")
                ], spacing=0
                )
            ]
        )


layout = html.Div(
    [       
    dbc.Row(
        html.Div([
            html.Br(),
            html.H2("Civilian Targeting (2017-2024)", 
                    style={'textAlign': 'center', 'color': 'red'},
                    # className='title-red'
                    ),        
                ]
            ),
        style={'padding-bottom': '2%', 'padding-top': '2%'},
    ),
  
        dbc.Row(
            [
                dbc.Col(dbc.Card(addCardBody('Total Fatalities', total_fatalities, '../assets/Mat_Kids.svg'), color="primary", inverse=True), width=3), 
                dbc.Col(dbc.Card(addCardBody('Total Events', total_events, '../assets/w-falling-bomb.svg'), color="primary", inverse=True), width=3), 
            ],  
            justify="center",
        ),
        html.Br(),

        dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=pieEvents(df))),
                dbc.Col(dcc.Graph(figure=pieFatalities(df))),
            ], 
        ),
        html.Br(),

        dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=tree(df))),
                dbc.Col(dcc.Graph(figure=map1(df))),
            ], 
        ),  
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(['All Sectors', 'Gaza Strip', 'West Bank'], 'All Sectors', id='dropdown-1', placeholder='Select Sector...',
                                     style={'color' : 'black', 'margin' : '20px'} ), width={"size": 6, "offset": 3}),
            ]
        ),

        dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=bar3(df, 'All Sectors'), id='graph-1'), width=6),
                dbc.Col(dcc.Graph(figure=bar4(df, 'All Sectors'), id='graph-2'), width=6),
            ], style={'margin-bottom' : 20}
        ),  
        


        dbc.Row(
            [
                dbc.Col(dcc.Graph(
                   figure=lineMonthlyEvents(df, 'All Sectors'), 
                    id='graph-3'), width=6),
                dbc.Col(dcc.Graph(
                   figure=lineMonthlyFatalities(df, 'All Sectors'), 
                    id='graph-4'), width=6),
            ], 
        ),


    ],
    style={
        'backgroundColor': '#212121',  # Dark background
        'color': '#fff',  # White text
    }
)

@callback(
    Output('graph-1', 'figure'),
    Output('graph-2', 'figure'),
    Output('graph-3', 'figure'),
    Output('graph-4', 'figure'),
    Input('dropdown-1', 'value')
)
def dropdown_selection(value):
    return bar3(df, value), bar4(df, value), lineMonthlyEvents(df, value), lineMonthlyFatalities(df, value)

