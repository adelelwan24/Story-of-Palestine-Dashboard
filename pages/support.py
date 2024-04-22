import dash
import pandas as pd
from dash import dcc, Input, Output, State, callback, clientside_callback, html
from dash_iconify import DashIconify

import dash_mantine_components as dmc
import dash_extensions as de

lottie_name = 'flag.json'
options = dict(loop=True, autoplay=True)

support_data = pd.read_excel('data/SupportPageData.xlsx')


dash.register_page(
    __name__,
    # path='/support',
    # image='home.png',
    # image='free-palestine.png',
    title='Story Of Palestine | Support',
    description=    "Stop the attacks on Gaza!"
                    "Take action for Palestine"
)

# Function to create a dmc.Card with customizable content
def create_card(image_src, title, description, button_link, button_text="Donate", button_color="blue"):
    return dmc.Card(
        children=[
            dmc.CardSection(
                # dmc.Image(src=image_src, height=160),
                dmc.Center(
                    html.Img(src=image_src, height=160, width=160,
                         style={
                             "width": "100%", 
                            # 'align': 'center',
                            #  "height": "100%", 
                             "objectFit": "fill"}),
                
                    ),
                ), 
            dmc.Stack([ 
                dmc.Group(
                    [
                        dmc.Text(title, weight=500),
                        dmc.Badge("On Sale", color="red", variant="light"),
                    ],
                    position="apart",
                    mt="md",
                    mb="xs",
                ),
                dmc.Text(description, size="sm", color="dimmed"),
                dmc.Button(
                    children=[
                        html.A(button_text, href=button_link, target="_blank")
                    ],
                    variant="light",
                    color=button_color,
                    fullWidth=True, mt="md",
                    radius="md",
                    bottom=0
                ),
                ], justify='flex-end', w="100%", spacing=0,
            )
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"width": 375, 'height': 375},
    )

layout = dmc.Grid(
    [
        dmc.Col(
            [   
                dmc.Stack(
                    children=[
                        dmc.Title('Stand With Palestine..', 
                                  style={'color': 'red'}, align='center', mt=30),
                        dmc.Stack(
                            [
                                dmc.Text(
                                    children=[
                                        "Stop the attacks on Gaza!",
                                    ],
                                    style={'color': 'gray', 'width': '100%'},
                                ),
                                dmc.Text(
                                    children=[
                                     "Take action for Palestine"                                    
                                     ],
                                    style={'color': 'gray', 'width': '100%'},
                                ),

                            ]
                        ),
                    ],
                    align='center',
                    # justify='flex-end',
                    className='stack-left-container',
                    spacing=20,
                )
            ],
            md=3, lg=12, mb=20
        ),
        dmc.Col(
            [
                #create_card(image_src= f"assets/support/{support_data['logo'][0]}", title=support_data['organization'][0], description=support_data['description'][0], button_link=support_data['donationLink'][0])
                dmc.Group(
                    [
                        # dmc.Text(support_data['organization'][0], weight=500),
                        # dmc.Badge("On Sale", color="red", variant="light"),
                        create_card(image_src=f"assets/support/{support_data['logo'][i]}", 
                            title=support_data['organization'][i], 
                            description=support_data['description'][i], 
                            button_link=support_data['donationLink'][i]) 

                        for i in range(10)
                    ],
                    # position="apart",
                    position="center",
                    mt="md",
                    mb="md", spacing=20,
                )

            ], md=9, lg=12
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
