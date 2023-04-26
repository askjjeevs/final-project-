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
    
def get_address_by_id(address_id):
    """This function should take an address ID as input and return the address object with that ID from the database."""
    return Address.query.get(address_id)

def get_activity_by_id(activity_id):
    """take an activity ID as input and return the activity object with that ID from the database"""

    return Activity.query.get(activity_id)

def get_activities_by_address(address_id):
    """take an address ID as input and return a list of activity objects associated with that address ID from the database."""
    
    return Activity.query.get(address_id)

def get_activities_by_user(user_id):
    """take a user ID as input and return a list of activity objects created by that user ID from the database."""

    return Activity.query.get(user_id)

def get_all_users():
    """This function should return a list of all user objects from the database."""
    return User.query.all()

def get_all_addresses():
    """ This function should return a list of all address objects from the database."""
    return Address.query.all()

def get_all_activities():
    """ This function should return a list of all activity objects from the database."""
    return Activity.query.all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)