import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server 

os.system('dropdb activity_matcher')
os.system('createdb activity_matcher')

model.connect_to_db(server.app)
model.db.create_all()

#Open the JSON files 
with open('data/addresses.json') as f:
    address_data = json.loads(f.read())

with open('data/activities.json') as f:
    activity_data = json.loads(f.read())

with open('data/users.json') as f:
    user_data = json.loads(f.read())

# Create and add addresses, store them in a list for fake data
addresses_in_db = []
for address in address_data:

    street_num, suit_num, street_name, city, state, zip_code = (
        address['street_num'],
        address['suit_num'],
        address['street_name'],
        address['city'],
        address['state'],
        address['zip_code'])
    
    db_address = crud.create_address(street_num, suit_num, street_name, city, state, zip_code)
    addresses_in_db.append(db_address)

model.db.session.add_all(addresses_in_db)
model.db.session.commit()

# Create users, store them in a list to use for fake data
users_in_db = []
for user in user_data:
    username, email, password, fname, lname, user_description = (
        user['username'],
        user['email'],
        user['password'],
        user['fname'],
        user['lname'],
        user['user_description'])
    
    db_user = crud.create_user(username, email, password, fname, lname, user_description)
    users_in_db.append(db_user)

model.db.session.add_all(users_in_db)
model.db.session.commit()

# Create activities, store them in a list to use for fake data
activities_in_db = []
for activity in activity_data:
    address_id, created_by, activity_name, activity_type,activity_date, activity_description = (
        activity['address_id'],
        activity['created_by'],
        activity['activity_name'],
        activity['activity_type'],
        datetime.strptime(activity['activity_date'], '%Y-%m-%d'),
        activity['activity_description'])

    db_activity = crud.create_activity(address_id, created_by, activity_name, activity_type,activity_date, activity_description)
    activities_in_db.append(db_activity)

model.db.session.add_all(activities_in_db)
model.db.session.commit()



    
