import dash
import pandas as pd
from dash import dcc, Input, Output, State, callback, clientside_callback, html
from dash_iconify import DashIconify

import dash_mantine_components as dmc
import dash_extensions as de

CHOROPLETH_INTERVAL = 50

url = 'https://lottie.host/bd952b99-002b-42d6-875e-57a7924ce27c/pEXSm4MJxX.json'
lottie_name = 'flag.json'
options = dict(loop=True, autoplay=True)

dash.register_page(
    __name__,
    path='/',
    image='free-palestine.png',
    title='Story Of Palestine | Home',
    description='Dive into the evolution of the Palestinian case with brief historical key events...'
                '',
    order=0,
)

layout = dmc.Grid(
    [
        dmc.Col(
            [   
                # de.Lottie(url=f'http://127.0.0.1:8050/loader?lottie=flag.json', options=options, isClickToPauseDisabled=True),
                de.Lottie(url=f'/loader?lottie={lottie_name}', options=options, 
                          isClickToPauseDisabled=True, width='50%', speed=1),
                # html.Img(src='assets\palestinian-map.png', style={'height' : '70vh'}),
                dmc.Stack(
                    children=[
                        dmc.Title('The full story of Palestine..', className='title-green',
                                  style={'color': 'green'}, align='center'),
                        dmc.Center(
                            [
                                dmc.Text(
                                    children=[
                                        "Dive into the evolution of the Palestinian case with brief historical key events..."
                                    ],
                                    style={'color': 'white', 'width': '50%'},
                                    align='center',
                                    id='main-text'
                                ),
                            ]
                        ),
                        dcc.Link(
                            [
                                dmc.Button(
                                    'start',
                                    id='start-btn',
                                    variant='filled',
                                    # variant='outline',
                                    # color='gray',
                                    color='green',
                                    style={'color' : 'black'},
                                    size='lg',
                                    uppercase=True,
                                    rightIcon=DashIconify(className='icon-color', 
                                                          icon='noto-v1:red-triangle-pointed-down', width=30)
                                ),
                            ],
                            href='/historical'
                        )
                    ],
                    align='center',
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
    id='home-grid',
    className='hide',
)




clientside_callback(
    """
    function(className) {
        return "fade-in";
    }
    """,
    Output('home-grid', 'className'),
    Input('home-grid', 'className'),
)
