import sqlite3
import json



with open('./DataSets/yelp_dataset/user.json') as review:
    conn = sqlite3.connect('./DataSets/yelpData.sqlite3')
    cur = conn.cursor()

    while True:
        json_string_obj = review.readline()
        if json_string_obj == '':
            break
        json_obj = json.loads(json_string_obj)

        user_id = json_obj['user_id']
        name = json_obj['name']
        review_count = json_obj['review_count']
        yelping_since = json_obj['yelping_since']
        friends = json_obj['friends']
        useful = json_obj['useful']
        funny = json_obj['funny']
        cool = json_obj['cool']
        fans = json_obj['fans']
        elite = json_obj['elite']
        average_stars = json_obj['average_stars']
        compliment_hot = json_obj['compliment_hot']
        compliment_more = json_obj['compliment_more']
        compliment_profile = json_obj['compliment_profile']
        compliment_cute = json_obj['compliment_cute']
        compliment_list = json_obj['compliment_list']
        compliment_note = json_obj['compliment_note']
        compliment_plain = json_obj['compliment_plain']
        compliment_cool = json_obj['compliment_cool']
        compliment_funny = json_obj['compliment_funny']
        compliment_writer = json_obj['compliment_writer']
        compliment_photos = json_obj['compliment_photos']

        cur.execute('INSERT INTO user (user_id, name, review_count, yelping_since, friends, useful, funny, cool, fans, elite, average_stars, compliment_hot, compliment_more, compliment_profile, compliment_cute, compliment_list, compliment_note, compliment_plain, compliment_cool, compliment_funny, compliment_writer, compliment_photos) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', [user_id, name, review_count, yelping_since, friends, useful, funny, cool, fans, elite, average_stars, compliment_hot, compliment_more, compliment_profile, compliment_cute, compliment_list, compliment_note, compliment_plain, compliment_cool, compliment_funny, compliment_writer, compliment_photos])

    conn.commit()