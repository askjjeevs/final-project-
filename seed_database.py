import os
import json
from random import choice, randint
from datetime import datetime, date, time
from model import db, User, Address, Activity, Subscriber, connect_to_db

import crud as crud
import server 
from flask import Flask
from passlib.hash import argon2

#os.system to automatically dropdb for us
os.system('dropdb activity_matcher')
os.system('createdb activity_matcher')

connect_to_db(server.app)
db.create_all()

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

    street_address, city, state, zip_code = (
        address['street_address'],
        address['city'],
        address['state'],
        address['zip_code'])
    
    db_address = crud.create_address(street_address=street_address, city=city, state=state, zip_code=zip_code)
    addresses_in_db.append(db_address)

db.session.add_all(addresses_in_db)
db.session.commit()

# Create users, store them in a list to use for fake data
users_in_db = []
for user in user_data:
    username, email, password, fname, lname, address_id, user_image_path, user_description = (
        user['username'],
        user['email'],
        user['password'],
        user['fname'],
        user['lname'],
        user['address_id'],
        user['user_image_path'],
        user['user_description']
        )
    
    db_user = crud.create_user(username=username, email=email, password=argon2.hash(password),
                               fname=fname, lname=lname, address_id=address_id, user_image_path=user_image_path, user_description=user_description)
    users_in_db.append(db_user)

db.session.add_all(users_in_db)
db.session.commit()


# Create activities, store them in a list to use for fake data
activities_in_db = []
for activity in activity_data:
    address_id, created_by, activity_name, activity_type, activity_date, activity_image_path, activity_description = (
        activity['address_id'],
        activity['created_by'],
        activity['activity_name'],
        activity['activity_type'],
        datetime.strptime(activity['activity_date'], '%Y-%m-%d'),
        activity['activity_image_path'],
        activity['activity_description'])
       
    db_activity = crud.create_activity(address_id=address_id, created_by=created_by, activity_name=activity_name, 
                        activity_type=activity_type, activity_date=activity_date, activity_image_path=activity_image_path, activity_description=activity_description)
    activities_in_db.append(db_activity)

db.session.add_all(activities_in_db)
db.session.commit()

subscribers_in_db = []
for idx in range(10):
    # choose a random user & activity
    user = choice(users_in_db)
    activity = choice(activities_in_db)

# Create a new subscriber and associate it with the chosen user and activity
    subscriber = Subscriber(activity_id=activity.activity_id, user_id=user.user_id)
    subscribers_in_db.append(subscriber)

# messages_in_db = []

    
db.session.add_all(subscribers_in_db)
db.session.commit()

