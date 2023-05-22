"""Crud operations"""

from model import db, User, Address, Activity, Subscriber, Message, connect_to_db

 # USERS 
def create_user(username, email, password, fname, address_id, lname, user_image_path=None, user_description=None):
    """Create and return a new user."""
    
    user = User(username=username, email=email, password=password, 
                fname=fname, lname=lname, address_id=address_id, user_image_path=user_image_path, user_description=user_description)

    return user

def get_user_by_email(email):
     """Return a user by email."""

     return User.query.filter(User.email == email).first()

def get_user_by_id(user_id):

    return User.query.get(user_id)

def get_all_users():
    """This function should return a list of all user objects from the database."""
    
    return User.query.all()

# ACTIVITIES 
def create_activity(address_id, created_by, activity_name, activity_type, activity_date,activity_image_path, activity_description):
    """Create and return a new activity."""
    
    activity = Activity(address_id=address_id, created_by=created_by, activity_name=activity_name, 
                        activity_type=activity_type, activity_date=activity_date, activity_image_path=activity_image_path, activity_description=activity_description)

    return activity

def get_activities():
    """This function should return a list of all activity objects from the database"""

    return Activity.query.all()

def get_activities_by_user(user_id):
    """get the activites that the user_id is subscribed to"""
    # return Activity.query.filter(User.user_id==user_id).join(User).all()
    # return Activity.query.filter(User.user_id==user_id).all()
    # return Subscriber.query.filter(User.user_id==user_id).join(User).all()
    return Activity.query.filter(Activity.users.any(User.user_id==user_id)).all()

def get_activities_user_created(user_id):
    """get all activities created by this user_id"""

    return Activity.query.filter(User.user_id==user_id).join(User).all()

def get_activity_by_id(activity_id):
    """take an activity ID as input and return the activity object with that ID from the database"""

    #return Activity.query.filter_by(activity_id=activity_id).all()
    return Activity.query.get(activity_id)

def get_activities_by_address(address_id):
    """take an address ID as input and return a list of activity objects associated with that address ID from the database."""
    
    return Activity.query.get(address_id)

def get_all_activities():
    """ This function should return a list of all activity objects from the database."""
    
    return Activity.query.all()

#ADDRESS
def create_address(street_address, city, state, zip_code):
    """Create and return a new address."""
    
    address = Address(street_address=street_address, city=city, state=state, zip_code=zip_code)
    return address 

def get_address_by_id(address_id):
    """This function should take an address ID as input and return the address object with that ID from the database."""
    
    return Address.query.get(address_id)

def get_address_by_user_id(user_id):
    """This function should take in the user_id as input and return the  first address for that specific user """
    
    return Address.query.filter(User.user_id==user_id).join(User).first()

def get_all_addresses():
    """ This function should return a list of all address objects from the database."""
    
    return Address.query.all()

# SUBSCRIBER 

def get_all_subscribers(activity_id):
    """This function should return a list of all subscriber objects from the database"""
    
    return Subscriber.query.all(activity_id)

def get_subscriber_by_user_and_activity(user_id, activity_id):

    return Subscriber.query.filter_by(user_id=user_id,activity_id=activity_id).first()

# MESSAGES

def create_message(activity_id, user_id, created_datetime, message_text):
    """Create and return a message"""

    message = Message(activity_id=activity_id, user_id=user_id, created_datetime=created_datetime, message_text=message_text)
    return message


def get_messages_by_activityId(activity_id):
    """Create and return a message"""

    return Message.query.filter(Activity.activity_id == activity_id).join(User).all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)