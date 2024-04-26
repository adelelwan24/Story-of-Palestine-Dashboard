import pandas as pd
import plotly.express as px

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc


dash.register_page(
    __name__,
    title='Internally Displaced People | Dashboard',
    order=3,
)

# Load data
df = pd.read_excel('data/WestBank_Displacement_dueto_Demolitions.xlsx', sheet_name='IDPs in WestBank since 2009')
df1 = pd.read_excel('data/WestBank_Displacement_dueto_Demolitions.xlsx', sheet_name='IDPs in WestBank by Year')
df2 = pd.read_excel('data/Gaza_IDPs.xlsx', sheet_name='Total')

# Function to center the title of a figure
def center_title(fig):
    fig.update_layout(title_x=0.5)

# Function to add title to y-axis
def add_yaxis_title(fig, title):
    fig.update_layout(yaxis_title=title)

# Create scatter plot
fig = px.scatter(
    df,
    x="Demolished Structures",
    y="IDPs",
    size="Affected people",
    color="Governorate",
    size_max=30,
    template='plotly_dark',
    title='IDPs in West Bank Since 2009',
)

# fig.update_layout(
#         font = dict(color = 'white'),
#         plot_bgcolor='rgba(0, 0, 0, 0.53)',
#         paper_bgcolor='rgba(0, 0, 0, 0.53)',)

fig1 = px.scatter(
    df1,
    x="Demolished Structures",
    y="IDPs",
    size="Affected people",
    color="Governorate",
    size_max=30,
    template='plotly_dark',
    title='Recent IDPs in West Bank',
)

fig2 = px.histogram(df1, x="Governorate", y="Demolished Structures", color='Year', template='plotly_dark', title='Recent Demolished Structures in West Bank')
fig3 = px.histogram(df, x="Governorate", y="Demolished Structures", template='plotly_dark', title='Demolished Structures in West Bank since 2009')
fig4 = px.line(df2, x="Date", y=df2.columns[2:5], template='plotly_dark',
              hover_data={"Date": "|%B %d, %Y"},
              title='Gaza IDPs')
# Add title to y-axis
add_yaxis_title(fig4, "Number of IDPs")

fig5 = px.bar(df2, x='Date', y=df2.columns[5:8], template='plotly_dark',
                      title='Gaza Shelters')
add_yaxis_title(fig5, "Number of Shelters")
# Store figures in a dictionary
figures = {'fig': fig, 'fig1': fig1, 'fig2': fig2, 'fig3': fig3, 'fig4': fig4, 'fig5': fig5}

# Apply center_title function to each figure
for name, figure in figures.items():
    center_title(figure)

import dash_bootstrap_components as dbc
from dash import html

def create_card(data_text, image_src, data_df, column_name, style=None):

  # Extract data from DataFrame
  data_value = data_df[column_name].sum()

  # Create card body with image, title, and description
  card_body = dbc.CardBody(
      [
          html.Img(src=image_src, className="card-img-top", style={'width': '100%'}),
          html.H5(data_value, className="card-title", style=style),
          html.P(data_text, className="card-text"),
      ]
  )

  return [card_body]

west_bank_2009_idp = create_card(
    data_text="Total Internally Displaced People",
    image_src="../assets/idp.svg",
    data_df=df,
    column_name="IDPs",
    style={'text-align': 'center'}
)

west_bank_2009_ds = create_card(
    data_text="Total demolished structures",
    image_src="../assets/broken-house.svg",
    data_df=df,
    column_name="Demolished Structures",
    style={'text-align': 'center'}
)

west_bank_2009_ap = create_card(
    data_text="Total affected people",
    image_src="../assets/aff.svg",
    data_df=df,
    column_name="Affected people",
    style={'text-align': 'center'}  # Center align the title
)

west_bank_idp = create_card(
    data_text="Total Internally Displaced People",
    image_src="../assets/idp.svg",
    data_df=df1,
    column_name="IDPs",
    style={'text-align': 'center'}
)

west_bank_ds = create_card(
    data_text="Total demolished structures",
    image_src="../assets/broken-house.svg",
    data_df=df1,
    column_name="Demolished Structures",
    style={'text-align': 'center'}
)

west_bank_ap = create_card(
    data_text="Total affected people",
    image_src="../assets/aff.svg",
    data_df=df1,
    column_name="Affected people",
    style={'text-align': 'center'}  # Center align the title
)

layout = html.Div(
    [   
        # dbc.Spinner(color="primary"),
        
        # dbc.Row(dbc.Col(html.Div(html.H2("IDPs in Gaza and WestBank"), style={'textAlign': 'center','color': 'red'}), style={'padding-bottom': '1%', 'padding-top': '1%'})),
        dbc.Row(dbc.Col(html.Div(html.H2("""Internally Displaced People""")
            , style={'textAlign': 'center','color': 'red'}), style={'padding-bottom': '1%', 'padding-top': '1%'})),
        
        dbc.Row([  
            dbc.Col(dbc.Card(west_bank_2009_idp, color="primary", inverse=True), style={'padding-left': '5%'}),  # Adjust padding as needed
            dbc.Col(dbc.Card(west_bank_2009_ds, color="danger", inverse=True)),
            dbc.Col(dbc.Card(west_bank_2009_ap, color="info", inverse=True), style={'padding-right': '5%'}),  # Adjust padding as needed
            dbc.Col(dbc.Card(west_bank_idp, color="primary", inverse=True), style={'padding-left': '5%'}),  # Include Gaza_idp card
            dbc.Col(dbc.Card(west_bank_ds, color="danger", inverse=True)),  # Assuming you have a gazastats_ds card
            dbc.Col(dbc.Card(west_bank_ap, color="info", inverse=True), style={'padding-right': '5%'}),  # Assuming you have a gazastats_ap card
        ],
            className="mb-4",  
        ),
        
        dbc.Row(
            [
                dbc.Col(html.Div(dcc.Graph(figure=fig)), style={'padding-left': '2%'}),
                dbc.Col(html.Div(dcc.Graph(figure=fig3))),
            ], 
        ),
        html.Br(),
        dbc.Row([  
            # dbc.Col(dbc.Card(west_bank_idp, color="primary", inverse=True), style={'padding-left': '30%'}),
            # dbc.Col(dbc.Card(west_bank_ds, color="danger", inverse=True)),
            # dbc.Col(dbc.Card(west_bank_ap, color="info", inverse=True), style={'padding-right': '30%'}),
        ],
            className="mb-4",  
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(html.Div(dcc.Graph(figure=fig1)), style={'padding-left': '2%'}),
                dbc.Col(html.Div(dcc.Graph(figure=fig2)))
            ], 
        ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(html.Div(dcc.Graph(figure=fig4)), style={'padding-left': '2%'}),
                dbc.Col(html.Div(dcc.Graph(figure=fig5)))
            ], 
        ),
        # html.Br(),
        # dbc.Row(
        #     [
        #         dbc.Col(html.Div(dcc.Graph(figure=fig6))),
        #     ], 
        # ),
    ]
)

if __name__ == "__main__":
    app.run_server(use_reloader=True)