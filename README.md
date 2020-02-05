# 1️⃣  Yelp Dataset Challenge Labs-19

You can find the project at [our Notion document](https://www.notion.so/Yelp-Dataset-Challenge-Labs-19-2c58ae1e609d480d806adb45f3fadf15).

## Contributors
|                                       [Maxime Vacher-Materno](https://github.com/maximematerno)                                        |                                       [Navaneeth Visagan](https://github.com/nvisagan)                                        |                                       [Jason Murphy](https://github.com/biovir3)                                        |                                                                              |                                                                              |
| :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: |
|                      [<img src="https://avatars3.githubusercontent.com/u/37785179?s=400&v=4" width = "200" />](https://github.com/maximematerno)                       |                      [<img src= "https://ca.slack-edge.com/T4JUEB3ME-ULXSN2E3Y-f0ccdecad793-512" width = "200" />](https://github.com/nvisagan)                       |                      [<img src="https://ca.slack-edge.com/T4JUEB3ME-UGTN60H8D-145a130154f9-512" width = "200" />](https://github.com/biovir3)                       |                                            |                     
|                 [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/)                 |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/honda0306)             |           [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/Mister-Corn)            |                      |
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) |
                    |                      

![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)
![Typescript](https://img.shields.io/npm/types/typescript.svg?style=flat)
[![Netlify Status](https://api.netlify.com/api/v1/badges/b5c4db1c-b10d-42c3-b157-3746edd9e81d/deploy-status)](netlify link goes in these parenthesis)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)



## Project Overview


1️⃣ [Trello Board](https://trello.com/b/rlQhiS9T/labs19-yelpdataset)

1️⃣ [Product Canvas](https://www.notion.so/ebe925e935614d9189c7729ee9e4cfd8?v=2246616d927646e3a63fe1bc8cc480c3)

Project Description

Yelp Dataset Challenge Labs 19 creating the next big data-driven ML powered product for Yelp using their dataset. https://www.yelp.com/dataset

Yelp is always looking for ways to improve the user having the best experience, and improved relevance of the top reviews shown is always a positive.


1️⃣ [Flask App Front End](https://yelp-challenge-adjusted-rating.herokuapp.com/predictions)

### Tech Stack
Python Language - data analysis, modeling, machine learning, etc.

Spacy/TextBLOB - NLP such as topic analysis, sentiment analysis, word embedding, etc.

Image Processing - Keras/PyTorch, etc.

AWS - DB, EMR, SageMaker, S3, etc.

Github - Version Control, documentation

Google Drive/AWS S3 - History data storage, Project management

OpenStack - Local cloud development (Specifically Zun, Nova, Cinder, Keystone, Freezer, Solum, and Horizon)

### 2️⃣ Predictions

NLP Sentiment Modeling , paticularly we are looking if we can predict the number of stars based on our entry of text

### 2️⃣ Explanatory Variables

-  Polarity : float which lies in the range of [-1,1] where 1 means positive statement and -1 means a negative statement.
-  Subjectivity: a float which lies in the range of [0,1] where closer to 1 refers to personal opinion, emotion or judgment

### Data Sources

- [Yelp Data] (https://www.yelp.com/dataset)

### Python Notebooks

[Intial Sentiment Analysis](https://github.com/Lambda-School-Labs/yelp-dataset-challenge-labs19.1/blob/master/SentimentAnalysis/SentimentVisuals.ipynb)

[WordCount Cleaning](https://github.com/Lambda-School-Labs/yelp-dataset-challenge-labs19.1/blob/master/EDA%20for%20Sentiment%20Based%20on%20Word%20Count.ipynb)

[Yelp NLP Modeling](https://github.com/Lambda-School-Labs/yelp-dataset-challenge-labs19.1/blob/master/yelp-challenge-adjusted-rating-app/notebooks/yelp_sentiment.ipynb)

### 3️⃣ How to connect to the web API



### 3️⃣ How to connect to the data API

The data API is deployed on heroku and not for personal use

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](./code_of_conduct.md.md). Please follow it in all your interactions with the project.

### Issue/Bug Request

 **If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**
 - Check first to see if your issue has already been reported.
 - Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
 - Create a live example of the problem.
 - Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes,  where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).

## Documentation

See [Backend Documentation](_link to your backend readme here_) for details on the backend of our project.

See [Front End Documentation](_link to your front end readme here_) for details on the front end of our project.

