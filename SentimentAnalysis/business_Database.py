import sqlite3
import json



with open('./DataSets/yelp_dataset/business.json') as business:
    conn = sqlite3.connect('./DataSets/yelpData.sqlite3')
    cur = conn.cursor()

    while True:
        json_string_obj = business.readline()
        if json_string_obj == '':
            break
        json_obj = json.loads(json_string_obj)
        business_id = json_obj['business_id']
        name = json_obj['name']
        address = json_obj['address']
        city = json_obj['city']
        state = json_obj['state']
        postal_code = json_obj['postal_code']
        latitude = json_obj['latitude']
        longitude = json_obj['longitude']
        stars = json_obj['stars']
        review_count = json_obj['review_count']
        is_open = json_obj['is_open']
        attributes_json = json_obj['attributes']
        categories_list = json_obj['categories']
        hours_json = json_obj['hours']

        attributes = json.dumps(attributes_json)
        categories = str(categories_list)
        hours = json.dumps(hours_json)

        cur.execute('''INSERT INTO business 
                       (business_id, name, address, city, state, postal_code, latitude, longitude, star, review_count, is_open, attributes, categories, hours)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                       [business_id, name, address, city, state, postal_code, latitude, longitude, stars, review_count, is_open, attributes, categories, hours])

    conn.commit()