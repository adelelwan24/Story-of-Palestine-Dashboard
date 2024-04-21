import dash
import json
import os
from dash import html, dcc, Output, Input, callback
from flask import send_from_directory, request
from assets.footer import footer
from pages.nav import navbar


app = dash.Dash(
    __name__,
    title='Story of Palestine',
    use_pages=True,
    # update_title=False,
    # suppress_callback_exceptions=True,
    # prevent_initial_callbacks=True,
    meta_tags=[
        {"name": "description", "content": "A Dash app focused on space exploration data."},
        {"name": "keywords", "content": "Space, Launch, Data, Visualization, Dash"}
    ], external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
)

server = app.server



#### Create end point to get local lottie(require to be from url)
@server.route("/loader", methods=['GET'])
def serving_lottie_loader():
    directory = os.path.join(os.getcwd(), "assets")
    lottie = request.args.get('lottie')
    return send_from_directory(directory, lottie)

app.layout = html.Div(
    [
        navbar(),
        dash.page_container,
        footer,
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
