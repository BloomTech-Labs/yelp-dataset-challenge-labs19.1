import sqlite3
import json



with open('./DataSets/yelp_dataset/review.json') as review:
    conn = sqlite3.connect('./DataSets/yelpData.sqlite3')
    cur = conn.cursor()

    while True:
        json_string_obj = review.readline()
        if json_string_obj == '':
            break
        json_obj = json.loads(json_string_obj)
        review_id = json_obj['review_id']
        user_id = json_obj['user_id']
        business_id = json_obj['business_id']
        stars = json_obj['stars']
        date = json_obj['date']
        text = json_obj['text']
        useful = json_obj['useful']
        funny = json_obj['funny']
        cool = json_obj['cool']
        #print(stars)
        cur.execute('INSERT INTO review (review_id, user_id, business_id, stars, date, text, useful, funny, cool) VALUES (?,?,?,?,?,?,?,?,?)', [review_id, user_id, business_id, stars, date, text, useful, funny, cool])
        #cur.execute("INSERT INTO review (review_id) VALUES (?)", [review_id])
    conn.commit()