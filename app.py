# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.read_csv(
    'https://raw.githubusercontent.com/ncmurenzi/SoftwareArtefact/main/survey-clean_version.csv')

fig = px.scatter(df, x="Age", y="Country", color="work_interfere", hover_name="no_employees", title="Country by Age when responding to wether they have interferance in their work",
                 log_x=True, size_max=80)


app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
