import sqlite3
import nltk
from textblob import TextBlob

conn = sqlite3.connect('./DataSets/yelpData.sqlite3')
cur = conn.cursor()
putcur = conn.cursor()

cur.execute('SELECT * FROM review')
sentimentList = list()
for review in cur:
    blobtext = TextBlob(review[5])
    #print(blobtext.sentiment)
    putcur.execute('INSERT INTO sentiment_textblob VALUES (?,?,?)', [review[0], blobtext.sentiment.polarity, blobtext.sentiment.subjectivity])
    conn.commit()
    #sentimentList.append([review[0],(blobtext.sentiment.polarity, blobtext.sentiment.subjectivity)])
    #review[9] = str(blobtext.sentiment)
    #print([review[0],(blobtext.sentiment.polarity, blobtext.sentiment.subjectivity)])
#print(sentimentList)
#text = "Hello this is a test"
#blobtext = TextBlob(text)

#print(blobtext.sentiment)