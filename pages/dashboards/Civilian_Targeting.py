from dash import dcc, html, callback, Input, Output

import dash

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
#import dash_mantine_components as dmc

dash.register_page(
    __name__,
    title='Civilian Targeting | Dashboard',
    order=2
)

########################################### Processing #############################################
df = pd.read_excel(r'data/palestine_hrp_civilian_targeting_events_and_fatalities_by_month-year_as-of-17apr2024.xlsx',sheet_name='Data')
#df_1 = pd.read_csv(r'D:\projectDV\Story-of-Palestine-Dashboard\data\fatalities_isr_pse_conflict_2000_to_2023 (Dataset) (1).csv')
total_fatalities = df['Fatalities'].sum()
total_events = df['Events'].sum()


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

def pie1(df):
    admin1_sum = df.groupby('Admin1')['Events'].sum().reset_index()
    fig = px.pie(admin1_sum, values='Events', names='Admin1',
                title='Events Distributions',
                # color_discrete_sequence=['#ff553b', 'blue'],
                template='plotly_white')
    
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, .53)',
        paper_bgcolor='rgba(0, 0, 0, .53)',
        margin=dict(l=50, r=50, t=50, b=50),
        font=dict(color='white')
    )
    #fig.layout.margin = dict(l=40, r=30, t=50, b=40)
    #html.Br()

    return fig


def pie2(df):
    admin1_sum = df.groupby('Admin1')['Fatalities'].sum().reset_index()
    fig = px.pie(admin1_sum, values='Fatalities', names='Admin1',
                title='Fatalities Distribution',
                color_discrete_sequence=['#ef553b', '#636efa'],
                template='plotly_white')
    fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0.53)',
            'paper_bgcolor': 'rgba(0,0,0,0.53)'
        },
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
    fig.update_layout(xaxis_tickangle=-45,
                       
                    width=600,  # Set the width of the plot
                    height=400,  # Set the height of the plot
                    plot_bgcolor='rgba(0, 0, 0, 0)',
                    paper_bgcolor='rgba(0, 0, 0, 0.53)'
                    )

    # Show the plot
    fig.update_layout(
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

    # Rotate x-axis labels for better readability
    fig.update_layout(xaxis_tickangle=-45,
                       
                    width=600,  # Set the width of the plot
                    height=400,  # Set the height of the plot
                    plot_bgcolor='rgba(0, 0, 0, 0)',
                    paper_bgcolor='rgba(0, 0, 0, 0.53)'
                    )

    # Show the plot
    fig.update_layout(
        font = dict(color = 'white'),
        legend=dict(x=0, y=1, bgcolor='rgba(255, 255, 255, 0.5)')  
    )

    return fig

def line3(df, value):
    tmp = filter_df(df, value)


    monthly_data = tmp.groupby('Month')['Fatalities'].sum().reset_index()
    fig = px.line(monthly_data, x='Month', y=['Fatalities'], markers=True,
                title='Monthly Fatalities')

    # Update layout for better visualization
    fig.update_layout(
        font = dict(color = 'white'),
        xaxis_title='Month',
        yaxis_title='Count',
        #xaxis={'categoryorder': 'array', 'categoryarray': month_names},
        width=600,  # Set the width of the plot
        height=400,  # Set the height of the plot
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        legend=dict(x=0, y=1, bgcolor='rgba(255, 255, 255, 0.5)')  # Place legend inside with white background

    )
    return fig

def line4(df, value):
    tmp = filter_df(df, value)

    monthly_data = tmp.groupby('Month')['Events'].sum().reset_index()
    fig = px.line(monthly_data, x='Month', y=['Events'], markers=True,
                title='Monthly Fatalities')

    # Update layout for better visualization
    fig.update_layout(
        font = dict(color = 'white'),
        xaxis_title='Month',
        yaxis_title='Count',
        #xaxis={'categoryorder': 'array', 'categoryarray': month_names},
        width=600,  # Set the width of the plot
        height=400,  # Set the height of the plot
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        legend=dict(x=0, y=1, bgcolor='rgba(255, 255, 255, 0.5)')  # Place legend inside with white background

    )
    return fig

def line5(df, value):
    tmp = filter_df(df, value)

    monthly_data = tmp.groupby('Month')['Events'].sum().reset_index()
    fig = px.line(monthly_data, x='Month', y=['Events'], markers=True,
                title='Monthly Events')

    # Update layout for better visualization
    fig.update_layout(
        font = dict(color = 'white'),
        xaxis_title='Month',
        yaxis_title='Count',
        #xaxis={'categoryorder': 'array', 'categoryarray': month_names},
        width=600,  # Set the width of the plot
        height=400,  # Set the height of the plot
        plot_bgcolor='rgba(0, 0, 0, 0.53)',
        paper_bgcolor='rgba(0, 0, 0, 0.53)',
        legend=dict(x=0, y=1, bgcolor='rgba(255, 255, 255, 0.5)')  # Place legend inside with white background

    )
    return fig

def line6(df, value):
    tmp = filter_df(df, value)


    monthly_data = tmp.groupby('Month')['Fatalities'].sum().reset_index()
    fig = px.line(monthly_data, x='Month', y=['Fatalities'], markers=True,
                title='Monthly Fatalities')

    # Update layout for better visualization
    fig.update_layout(
        font = dict(color = 'white'),
        xaxis_title='Month',
        yaxis_title='Count',
        #xaxis={'categoryorder': 'array', 'categoryarray': month_names},
        width=600,  # Set the width of the plot
        height=400,  # Set the height of the plot
        plot_bgcolor='rgba(0, 0, 0, 0.53)',
        paper_bgcolor='rgba(0, 0, 0, 0.53)',
        legend=dict(x=0, y=1, bgcolor='rgba(255, 255, 255, 0.5)')  # Place legend inside with white background

    )
    return fig

def tree1(df):
    # data_2023 = df[(df['Month'] >= 'January') & (df['Year'] == 2023)]
    d = df[['Admin1', 'Admin2']].value_counts()

    data2 = d.to_frame().reset_index()
    data2.columns = ['Admin1', 'Admin2', 'Fatalities']

    fig = px.treemap(data2, path=['Admin1', 'Admin2'], values='Fatalities',
                    title='Where is the most Fataliteies?',
                    color_continuous_scale='RdBu')
    
    fig.update_layout( 
        plot_bgcolor='rgba(0, 0, 0, .53)',
        paper_bgcolor='rgba(0, 0, 0, .53)',
        font = dict(color = 'white'))
    # fig.data[0].textinfo = 'label+text+value+current path'
    fig.data[0].textinfo = None
    # fig.layout.hovermode = True
    return fig

# def tree1(df_1):

#     d = df_1['ammunition'].value_counts()
#     data = d.to_frame().reset_index()
#     data.columns = ['Ammunition', 'Deaths']

#     # Create Treemap chart
#     fig = px.treemap(data, path=['Ammunition'], values='Deaths', custom_data=['Deaths'],
#                     color_continuous_scale='RdBu',
#                     title='Most Deaths Causing Ammunition')
#     fig.update_layout( 

#         plot_bgcolor='rgba(0, 0, 0, .53)',
#         paper_bgcolor='rgba(0, 0, 0, .53)',
#         font = dict(color = 'white'))
#     # this is what I don't like, accessing traces like this
#     fig.data[0].textinfo = 'label+text+value+current path'

#     fig.layout.hovermode = False
#     return fig

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
        title='Fataliteies in Palastine',
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

    return fig


########################################### ####### #################################################


def addCardBody(title, value):
    return dbc.CardBody(
            [
                html.H4(title, className="card-title"),
                html.P(value, className="card-text"),
            ]
        )



layout = html.Div(
    [       
    dbc.Row(
        html.Div(
            html.H2("Civilian Targeting (2017-2024)", style={'textAlign': 'center', 'color': 'white'}),
            style={'border': '2px solid black', 'padding': '10px'}
        ),
        style={'padding-bottom': '2%', 'padding-top': '2%'},
    ),
  
        dbc.Row(
            [

                dbc.Col(dbc.Card(addCardBody(total_fatalities, 'Total Fatalities'), color="danger", inverse=True), width=3), 
                # dbc.Col(dcc.Dropdown(['All', 'Gaza Strip', 'West Bank'], 'All', id='dropdown-1', )),
                dbc.Col(dbc.Card(addCardBody(total_events, 'Total Events'), color="danger", inverse=True), width=3), 
                #dbc.Col(dcc.Dropdown(['All', 'Gaza Strip', 'West Bank'], 'All', id='dropdown-1', ), width=6),
                #dbc.Col(dcc.Graph(figure=bar4(df)), width=6),
            ],  
            # style = {'padding-left' : '10%', 'padding-right': '10%'} , 
            justify="center",
        ),
        html.Br(),

        dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=pie1(df))),
                
                dbc.Col(dcc.Graph(figure=pie2(df))),
            ], 
        ),
        html.Br(),

        dbc.Row(
            [
                dbc.Col(dcc.Graph(figure=tree1(df))),
                dbc.Col(dcc.Graph(figure=map1(df))),
            ], 
        ),  
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(['All', 'Gaza Strip', 'West Bank'], 'All', id='dropdown-1', 
                                     style={'color' : 'black', 'margin' : '20px'} ), width={"size": 6, "offset": 3}),
                # dbc.Col(
                #     dmc.MultiSelect(
                #         label="Select Reigon",
                #         placeholder="Select as you like!",
                #         id="multi-select",
                #         value=["Gaze Stip", "West Bank"],
                #         data=[
                #             {"value": "Gaze Stip", "label": "Gaze Stip"},
                #             {"value": "West Bank", "label": "West Bank"},
                #         ],
                #         w=400,
                #         mb=10,
                #         pos='center'
                #     ), align='center', width=12
                # ),
            ]
        ),

        dbc.Row(
            [

                dbc.Col(dcc.Graph(
                   figure=bar3(df, 'All'), 
                    id='graph-1'), width=6),
                dbc.Col(dcc.Graph(
                   figure=bar4(df, 'All'), 
                    id='graph-2'), width=6),
				# style = {'padding-right' : '2%'} 
            ], style={'margin-bottom' : 20}
        ),  
        


        dbc.Row(
            [

                dbc.Col(dcc.Graph(
                   figure=line5(df, 'All'), 
                    id='graph-3'), width=6),
                dbc.Col(dcc.Graph(
                   figure=line6(df, 'All'), 
                    id='graph-4'), width=6),
				# style = {'padding-right' : '2%'} 
            ], 
        ),


    ]
)

@callback(
    Output('graph-1', 'figure'),
    Output('graph-2', 'figure'),
    Output('graph-3', 'figure'),
    Output('graph-4', 'figure'),
    Input('dropdown-1', 'value')
)
def dropdown_selection(value):
    print(value)
    return bar3(df, value), bar4(df, value), line5(df, value), line6(df, value)


# @callback(
#     Output('graph-1', 'figure'),
#     Output('graph-2', 'figure'),
#     Output('graph-3', 'figure'),
#     Output('graph-4', 'figure'),
#     Input('multi-select', 'value')
# )
# def multi_selection(value):
#     if len(value) == 1:
#         value = value[0]
#     else:
#         value = 'All'
#     return bar3(df, value), bar4(df, value), line5(df, value), line6(df, value)


if __name__ == "__main__":
    app.run_server(debug=True)
# app.run_server(use_reloader=True)