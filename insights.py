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
            #### Data Science - Yelp Feelers
            This is the Data Science portion for an Application that uses Machine Learning to build a Yelp Adjusted Ratings App based on User's text review which is then put through a rigorous Sentiment Analysis.            
            #### Flowchart
            """,
        className='mb-4'),
        (
            html.Img(src='assets/FlowChart.png', style= {'width': '100%', 'display': 'inline-block'}, alt="Responsive image", className='mb-4')          
        ),
        dcc.Markdown(
            """  
             #### Project Info   
            For the Data Science portion of this application, we used this Kaggle Yelp Dataset. Within it, you will find a number of reviews from Yelp Users on a variety of places ranging from restaurants and bars to salons and plumbers. 
            For this project, we were tasked with analyzing taco restaurants just due to the sheer volume of observations in the dataset(5 million + rows). We used a variety of tools such as Pandas, Gensim, and Sklearn for our simpler models. 
            We used TensorFlow for experimentation with neural networks on our data. Our primary strategy was Sentiment Analysis using a vectorizer, a scaler, then both regression/classification models. We found regression to be the best approach for our particular problem, 
            and we trained the tokenized/vectorized data on our target(the yelp star ratings). We found the linear model actually worked nicely in this case because it provides a more accurate sentiment rating because of the weights of certain words used. 
            Whereas something highly accurate like a neural net did perform incredibly well, but our goal wasn't to perfectly predict what the star ratings were, it was to give an adjusted rating that was a better representation of the actual true rating of a restaurant based on what the user said. From there, we worked extensively with our back-end architect to get the data in a format that he could easily work with. After some trials we finally got it nailed down to a succint method for getting our data to the back end, and from there we could easily tinker with and adjust data as the rest of the team needed.          
            """,
        className='mb-4'),
        
        dcc.Markdown(
            """ 
            #### Logs       
            October 21, 2019 Exploratory Data Analysis & Initial Modeling, Mock Data To Backend

            October 22, 2019 Optimize Model for better accuracy, Set up End points for Backend

            October 23, 2019 Completed the bulk of both MVP and Stretch Requirements. DS team is on stand-by in case additional data engineering or model optimization is required.

            October 24, 2019 Final day, just standing by incase our team needs us. Otherwise we're making little tweaks here and there, improving what can be improved upon, and otherwise just allow the rest of the areas of our team to do what they do best.        
            """,
        className='mb-4'),
        
        dcc.Markdown(
            """
            #### Contributing         
            Pull requests are welcome. However for major changes, please open an issue first to discuss what you would like to change.

            Please make sure to update tests as appropriate.           
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