"""Crud operations"""

from model import db, User, Address, Activity, Subscriber, connect_to_db

def create_user(username, email, password, fname, lname, address_id, user_description):
    """Create and return a new user."""
    
    user = User(username=username, email=email, password=password, 
                fname=fname, lname=lname,address_id=address_id, user_description=user_description)

    return user

def create_address(street_num, suit_num, street_name, city, state, zip_code):
    """Create and return a new address."""
    
    address = Address(street_num=street_num, suit_num=suit_num, 
                      street_name=street_name, city=city, state=state, zip_code=zip_code)

    return address 

def create_activity(address_id, created_by, activity_name, activity_type, activity_date, activity_description):
    """Create and return a new activity."""
    
    activity = Activity(address_id=address_id, created_by=created_by, activity_name=activity_name, 
                        activity_type=activity_type, activity_date=activity_date, activity_description=activity_description)

    return activity

def get_activities():
    """This function should return a list of all activity objects from the database"""

    return Activity.query.all()

def get_user_by_email(email):
     """Return a user by email."""

     return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):

    return User.query.get(user_id)

def get_activities_by_user(user_id):
    
    return Activity.query.get(user_id)



if __name__ == '__main__':
    from server import app
    connect_to_db(app)