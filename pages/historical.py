import dash
from dash import dcc, callback, Input, Output, html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

import pandas as pd

story = pd.read_excel('data/story.xlsx')

dash.register_page(
    __name__,
    title='Story Of Palestine | Historical',
    description="Dive into the evolution of the Palestinian case with brief historical key events...",
    image='palestinian-map.png',
    order=1,
)

all_years = list(story['year'])
all_ids = list(story['id'])

MIN, MAX = min(all_ids), max(all_ids)


def left_content(*, title, date, description, image, tooltip_text):
    tooltip = dbc.Tooltip(
        tooltip_text,
        target=f"image-tooltip-{image}",
        placement="auto",
        # You can customize the appearance of the tooltip here
        style={"color": "black"},
    )

    return [
        dmc.Space(h='15px'),
        dmc.Title(title, id='story-title', order=1, className='title-green'),
        dmc.Title(date, id='story-date', order=2, className='title-red', align='center'),
        html.Img(
            id=f"image-tooltip-{image}",
            src=f'assets/story/{image}',
            style={'object-fit': 'contain',
                   'height': '30vh', 'border-radius': '10%'}
        ),
        tooltip,
        dmc.Text(description,
                  style={'color': 'white',
                         'width': '75%',
                         '-webkit-text-stroke-width': '.5px',
                         'background': 'rgba(0, 0, 0, 0.53)'
                         },
                  ),
    ]

def right_content(*, image):
        

    
    return [
        dmc.Stack([
            dmc.Badge("Palestine", color="green", size='md', fullWidth=True),
            dmc.Badge("Occupation", color="red", size='md', fullWidth=True),
        ], 
        #  position='apart', grow=True, 
        spacing='sm', my=25, mx=0
        ),

        dmc.Container(
            children=[
            html.Img(src=f'assets/map/{image}',  
                        style={'object-fit': 'contain', 'border' : '5px', 
                               'height' : '70vh', 'border-radius': '10%'}
                    ) if image else None,
            ],
            px=0,
        ),
    ]


layout = dmc.Grid(
    [
        dmc.Col(
            children=[
                dmc.Stack(
                    id='historical-content',
                    align='center',
                    # justify='flex-end',
                    className='stack-left-container',
                    spacing=10,
                    h='80vh',
                    mah='90%',
                ),
                dmc.Container(
                    [
                        dcc.Slider(
                            id='year-slider',
                            value=MIN,
                            min=MIN,
                            max=MAX,
                            step=1,
                            marks={ str(id) : { 'label':str(year), 'style' : {
                                'display': 'None',
                                'transform' : 'rotate(90deg)'
                            }} for year, id in zip(all_years, all_ids)},
                            
                            tooltip={"always_visible": True, "placement": "bottom",
                                     "style": {"color": "LightSteelBlue", "fontSize": "15px"},
                                     "transform" : "tranform_slider_label",
                                    }
                        ),
                    ],
                    mt=40,
                    w='80%',
                    style= {'bottom': 20}
                ),
            ],
            md=12, lg=9
        ),
        dmc.Col(
            [
                dmc.Stack(
                    id='map',
                    align='center',
                    justify='center',
                    className='right-container',
                    style={'height': '100%'},
                    mx=0,
                    px=0
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
)
def update_historical_content(value):
    if value == 0:
        value = story['year'].min()

    df = story[story['id'] == value]

    return left_content(
        title=df['event'],
        date=df['year'],
        description=df['notes'],
        # image=img,
        image=df['picture1'].values[0],
        tooltip_text=df['DIS1'].values[0]
    ), 'hide'


@callback(
    Output('historical-content', 'className', allow_duplicate=True),
    Input('historical-content', 'className'),
    prevent_initial_call=True
)
def animation(_):
    return 'fade-in'


@callback(
    Output('map', 'children'),
    # Output('map', 'className'),
    Input('year-slider', 'value'),
)
def update_map(value):
    value = story[story['id'] == value]['year'].values[0]

    if value > 2014:
        img = '2015.png'
    elif value > 1959:
        img = '1960.png'
    elif value > 1946:
        img = '1947.png'
    elif value > 1917:
        img = '1918.png'
    else:
        img = 'free.png'

    return right_content(image=img,)
# , 'hide'

@callback(
    Output('map', 'className', allow_duplicate=True),
    Input('map', 'className'),
    prevent_initial_call=True
)
def animation(_):
    return 'fade-in'