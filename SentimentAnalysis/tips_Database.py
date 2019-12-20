import sqlite3
import json



with open('./DataSets/yelp_dataset/tip.json') as tip:
    conn = sqlite3.connect('./DataSets/yelpData.sqlite3')
    cur = conn.cursor()

    while True:
        json_string_obj = tip.readline()
        if json_string_obj == '':
            break
        json_obj = json.loads(json_string_obj)

        user_id = json_obj['user_id']
        business_id = json_obj['business_id']
        compliment_count = json_obj['compliment_count']
        date = json_obj['date']
        text = json_obj['text']

        cur.execute('INSERT INTO tip (text, date, compliment_count, business_id, user_id) VALUES (?,?,?,?,?)', [text, date, compliment_count, business_id, user_id])

    conn.commit()