import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """        
            #### Data Science - Yelp Challenge Adjusted Ratings App
            This is the Data Science portion for an Application that uses Machine Learning to build a Yelp Challenge Adjusted Ratings App based on User's text review which is then put through a rigorous Sentiment Analysis.            
            #### Flowchart
            """,
        className='mb-4'),
        (
            html.Img(src='assets/FlowChart.png', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        dcc.Markdown(
            """  
             #### Project Info   
            For the Data Science portion of this application, we used Yelp Challenge Dataset. Within it, you will find a number of reviews from Yelp Users on a variety of places ranging businesses. 
            For this project, we used a variety of tools such as Pandas, Gensim, and Sklearn for our simpler models. 
            We used TensorFlow for experimentation with neural networks on our data. Our primary strategy was Sentiment Analysis using a vectorizer, a scaler, then both regression/classification models. We found regression to be the best approach for our particular problem, 
            and we trained the tokenized/vectorized data on our target. We found the linear model actually worked nicely in this case because it provides a more accurate sentiment rating because of the weights of certain words used. 
                   
            """,
        className='mb-4'),
        
        
        
        dcc.Markdown(
            """
            #### License 
            MIT
            """,   
        className='mb-4'),
             
    ],
)

layout = dbc.Row([column1])