import dash
import pandas as pd
from dash import dcc, Input, Output, State, callback, clientside_callback, html
from dash_iconify import DashIconify

import dash_mantine_components as dmc
import dash_extensions as de

lottie_name = 'flag.json'
options = dict(loop=True, autoplay=True)

dash.register_page(
    __name__,
    # path='/support',
    # image='home.png',
    # image='free-palestine.png',
    title='Story Of Palestine | Support',
    description='Explore the world of space exploration through a 3D rotating globe, showcasing '
                'the number of launches by country since the dawn of the space age'
)

layout = dmc.Grid(
    [
        dmc.Col(
            [   
                dmc.Stack(
                    children=[
                        dmc.Title('The full story about palestine..', 
                                  style={'color': 'green'}, align='center'),
                        dmc.Center(
                            [
                                dmc.Text(
                                    children=[
                                        "Dive into the ture story of palestine"
                                        "milestones. Explore real-time data visualizations and get insights into the "
                                        "future of space exploration."
                                    ],
                                    style={'color': 'white', 'width': '50%'},
                                    align='center',
                                    id='main-text'
                                ),
                            ]
                        ),
                        dcc.Link(
                            [
                                
                            ],
                            href='/historical'
                        )
                    ],
                    align='center',
                    # justify='flex-end',
                    className='stack-left-container',
                    spacing=30,
                )
            ],
            md=12, lg=8
        ),
        dmc.Col(
            [
                dmc.Center(
                    className='right-container',
                    id='right-container',
                    children=[
                        dmc.Loader(
                            color="blue",
                            size="md",
                            variant="oval"
                        ),
                        html.Img(src='assets\pennant.png', height='100%'),
                    ]
                ),
            ], md=12, lg=4
        ),
    ],
    id='support-grid',
    className='hide',
)


clientside_callback(
    """
    function(className) {
        return "fade-in";
    }
    """,
    Output('support-grid', 'className'),
    Input('support-grid', 'className'),
)
