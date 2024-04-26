import dash
import pandas as pd
from dash import dcc, Input, Output, State, callback, clientside_callback, html
from dash_iconify import DashIconify

import dash_mantine_components as dmc
import dash_extensions as de

lottie_name = 'flag.json'
options = dict(loop=True, autoplay=True)

support_data = pd.read_excel('data/SupportPageData.xlsx')
support_data2 = pd.read_excel('data/SupportData_2.xlsx')

dash.register_page(
    __name__,
    title='Story Of Palestine | Support',
    description=    "Stop the attacks on Gaza!"
                    "Take action for Palestine",
    order=4,
)

# Function to create a dmc.Card with customizable content
def create_card(image_src, title, description, button_link, button_text, info_link=None, button_color="blue"):
    return dmc.Card(
        children=[
            dmc.CardSection(
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
                        dmc.Badge(dmc.Anchor("info", href=info_link), color="red", variant="light") if info_link is not None else None
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
        style={"width": 375, 'height': 390},
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
                                        "Stop the attacks on Gaza!, Take action for Palestine",
                                    ],
                                    style={'color': 'gray', 'width': '100%'},
                                ),
                                dmc.Select(
                                    id='support-dropdown',
                                    data=["Support", "Act"],
                                    searchable=True,
                                    value='Support',
                                    nothingFound="No options found",
                                    style={"width": 200},
                                ),
                            ]
                        ),
                        dmc.Title('Support Palestine', 
                                  style={'color': 'red'}, align='center', mt=30),
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
                dmc.Group(
                    id='card-group',
                    children = [  
                        create_card(image_src=f"assets/support/{support_data['logo'][i]}", 
                            title=support_data['organization'][i], 
                            description=support_data['description'][i], 
                            button_link=support_data['donationLink'][i],
                            info_link=support_data['learnMoreLink'][i],
                            button_text="Donate") 
                        for i in range(len(support_data))
                    ],
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

@callback(
    Output('card-group', 'children'),
    Output('card-group', 'className', allow_duplicate=True),
    Input('support-dropdown', 'value'),
    prevent_initial_call=True
)
def update_card_group(value):
    if value == 'Support':
        return [
                        create_card(image_src=f"assets/support/{support_data['logo'][i]}", 
                            title=support_data['organization'][i], 
                            description=support_data['description'][i], 
                            button_link=support_data['donationLink'][i],
                            info_link=support_data['learnMoreLink'][i],
                            button_text="Donate") 
                        for i in range(len(support_data))
                ], 'hide'
    elif value == 'Act':
        return [    create_card(image_src=f"assets/support/{support_data2['logo'][i]}", 
                        title=support_data2['organization'][i], 
                        description=support_data2['description'][i], 
                        button_link=support_data2['link'][i],
                        button_text="Act") 
                        for i in range(len(support_data2))
                ], 'hide'

clientside_callback(
    """
    function(className) {
        return "fade-in";
    }
    """,
    Output('support-grid', 'className'),
    Input('support-grid', 'className'),
)

@callback(
    Output('card-group', 'className', allow_duplicate=True),
    Input('card-group', 'className'),
    prevent_initial_call=True
)
def animation(_):
    return 'fade-in'

# link = "dashboard link";
# text = "Learn more about the story of Palestine, the status of Gaza, Israeli war crimes. Support Palestine! ";