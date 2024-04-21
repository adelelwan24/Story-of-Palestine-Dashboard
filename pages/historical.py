import dash
from dash import dcc, callback, Input, Output, ctx, no_update, html
import dash_mantine_components as dmc
import dash_extensions as de
from dash_iconify import DashIconify
from random import sample
import json
import datetime
import pandas as pd

story = pd.read_excel('data/story.xlsx')
# story = pd.read_excel('data/story.csv')

LOTTIE_URL = 'https://lottie.host/bd952b99-002b-42d6-875e-57a7924ce27c/pEXSm4MJxX.json'
LOTTIE_OPTIONS = dict(loop=True, autoplay=True)

dash.register_page(
    __name__,
    # image='historical.png',
    image='p.png',
    title='Space Exploration | Historical',
    description='Dive into the key milestones of space exploration, presented in a unique cytoscape constellation '
                'format. Each point represents a significant event, complete with descriptions and images'
)


all_years = list(story['year'])
MIN_YEARS, MAX_YEARS = min(all_years), max(all_years)


def right_content(*, title, date, description, image):
    print(image)
    return [
            dmc.Space(h='40px'),
            dmc.Title(title, id='story-title', order=1,
                        style={'color': 'green'}, align='center'
                        ),

            dmc.Title(date, id='story-date', order=2,
                style={'color': 'red'}, align='center'),

            # html.Img(src='assets/free-palestine.png',  
            html.Img(src=f'assets/story/{image}',  
                        style={'object-fit': 'contain', 
                               'height' : '30vh', 'border-radius': '10%'}
                    ),
            dmc.Center(
                [
                    dmc.Text(description,
                        style={'color': 'white', 'width': '50%'},
                        align='center',
                        id='story-desc'
                    ),
                ]
            )
        ]

# def right_content(*, title, date, description, image):
#     return [
#         dmc.Title(title, color='white', align='center'),
#         dmc.Title(date, order=3, color='white',
#                   align='center'),
#         dmc.Container(
#             children=[
#                 dmc.Image(
#                     src=f'assets/story/{image}',
#                     alt='historical',
#                     width='100%',
#                     height='100%',
#                     #radius=4,
#                     withPlaceholder=True,
#                     #style={'border-radius': '50%'},
#                     styles={
#                         # 'placeholder': {'background-color': '#000000'},
#                         'image': {'border-radius': '50%', 'object-fit': 'cover'}
#                     },
#                 ) if image else None
#             ],
#             px=0,
#         ),
#         dmc.Text(description, color='white', align='center')
#     ]
# def left_content(*, title, date, description, image):
#     return 


layout = dmc.Grid(
    [
        dmc.Col(
            children=[
                dmc.Stack(
                    id='historical-content',
                    # children=[
                    #     dmc.Space(h='40px'),
                    #     dmc.Title('The full story about palestine..', id='story-title', order=1,
                    #               style={'color': 'green'}, align='center', fz=46
                    #               ),

                    #     dmc.Title('10, Octobar 2023', id='story-date', order=2,
                    #         style={'color': 'red'}, align='center'),

                    #     # html.Img(src='assets/free-palestine.png',  
                    #     html.Img(src='assets/free.png',  
                    #              style={'object-fit': 'contain', 'height' : '30vh', 'border-radius': '20%'}
                    #             ),
                    #     dmc.Center(
                    #         [
                    #             dmc.Text(
                    #                 children=[
                    #                     "Dive into the ture story of palestine"
                    #                     "milestones. Explore real-time data visualizations and get insights into the "
                    #                     "future of space exploration."
                    #                 ],
                    #                 style={'color': 'white', 'width': '50%'},
                    #                 align='center',
                    #                 id='story-desc'
                    #             ),
                    #         ]
                    #     )
                    # ],
                    align='center',
                    # justify='flex-end',
                    className='stack-left-container',
                    spacing=30,
                    h='80vh',
                    mah='90%',
                ),
                dmc.Container(
                    [
                        dcc.Slider(
                            id='year-slider',
                            value=MIN_YEARS,
                            min=MIN_YEARS,
                            max=MAX_YEARS,
                            step=None,
                            marks={ str(years) : { 'label':str(years), 'style' : {
                                'display': 'None'
                            }} for years in all_years},
                            # marks={str(years):str(years) for years in all_years},
                            tooltip={"placement": "bottom", "always_visible": True,}
                            # style={'width': '50%'},
                        ),
                    ],
                    mt=50,
                    mb=50,
                    # position='center',
                    style={
                        # 'position': 'fixed', 
                           'bottom': 20
                           }
                ),
            ],
            md=12, lg=9
        ),
        dmc.Col(
            [
                dmc.Stack(
                    id='map',
                    # id='historical-content',
                    align='center',
                    justify='center',
                    spacing='25px',
                    style={'height': '100%'},
                    mb=50
                ),
            ],
            md=12, lg=3
        ),
    ],
)



@callback(
    Output('historical-content', 'children'),
    Output('historical-content', 'className'),
    Input('year-slider', 'value'),
    # prevent_initial_call=True
)
def update_historical_content(value):
    # input_id = list(ctx.triggered_prop_ids)[0].split('.')[-1]
    print(value)
    df = story[story['year'] == value]
    # if input_id == 'elements':
    # return left_content(
    return right_content(
        title=df['event'],
        date=df['year'],
        description=df['notes'],
        image=df['picture1'].values[0],
        # image=None
    ), 'hide'
    # else:
    #     if not any(node_data[key] for key in node_data if key != 'id'):
    #         return no_update
    #     return left_content(
    #         date=node_data['DATE'],
    #         country=node_data['COUNTRY'],
    #         description=node_data['DESCRIPTION'],
    #         image=node_data['IMAGE_LINK']
    #     ), 'hide'


@callback(
    Output('historical-content', 'className', allow_duplicate=True),
    Input('historical-content', 'className'),
    prevent_initial_call=True
)
def animation(_):
    return 'fade-in'