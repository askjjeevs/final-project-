"""Crud operations"""

from model import db, User, Address, Activity, Subscriber, connect_to_db

def create_user(username, email, password, fname, lname, user_description):
    """Create and return a new user."""
    
    user = User(username=username, email=email, password=password, 
                fname=fname, lname=lname, user_description=user_description)

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

def get_user_by_username(username):
    """ return the user object with that username from the database. """
    user = User.query.filter_by(username=username).first()

    return user 

# def get_user_by_email(email):
#     """Takes an email as input and returns the user object with that email from the database"""
    
# def get_address_by_id(address_id):
#     """This function should take an address ID as input and return the address object with that ID from the database."""



# if __name__ == '__main__':
    from server import app
    connect_to_db(app)