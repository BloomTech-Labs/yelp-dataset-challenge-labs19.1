import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
from app import app
import pandas as pd

pipeline = load('assets/pipeline.joblib')

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions
            """, className='mb-3'
        ),
        dcc.Input(id='tokens',
    placeholder='Enter your review here!!...',
    type='text',
    value=''
),  
               
        # for _ in ALLOWED_TYPES
    ],
    md=7,
)

column2 = dbc.Col(
    [
        html.H2('Adjusted Ratings', className='mb-5'), 
        html.Div(id='prediction-content', className='lead'),
        html.Img(src='assets/AirCut.jpeg', className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])


@app.callback(
    Output('prediction-content', 'children'),
    [Input('tokens','value')],
)


def predict(tokens):
    # df = pd.DataFrame(
    #     columns=['tokens'], 
    #     data=[[tokens.astype(str)]]
    # )
    y_pred = pipeline.predict([tokens])[0]
    return f'{y_pred:10,.2f} adjusted sentiment rating'