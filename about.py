import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [   
    
        (
            html.Img(src='assets/ben.png', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        dcc.Markdown(
            """
            #### Benjamin Lopez        
            #### Team Leader 
            """,
        className='mb-4'),
        
             
    ],
)

column2 = dbc.Col(
    [   
       (
            html.Img(src='assets/jason.jpg', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        dcc.Markdown(
            """ 
            #### Jason Murphy        
            #### Data Scientist 
            """,
        className='mb-4'),
    ]
)

column3 = dbc.Col(
    [  
        (
            html.Img(src='assets/navo.jpg', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        dcc.Markdown(
            """ 
            #### Navaneeth Visagan       
            #### Data Scientist 
            """,
        className='mb-4'),
    ]
) 

column4 = dbc.Col(
    [  
        (
            html.Img(src='assets/maxime.jpg', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        dcc.Markdown(
            """ 
            #### Maxime Vacher-Materno       
            #### Data Scientist 
            """,
        className='mb-4'),
    ]
)

layout = dbc.Row([column1,column2,column3,column4])