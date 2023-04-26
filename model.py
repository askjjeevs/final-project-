"""Models for creating Activity Matcher App"""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ ="users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True,)
    password = db.Column(db.String,)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey("addresses.address_id"), nullable=True) #nullable = True ( means this field does not need to be populated)
    user_description = db.Column(db.Text, nullable=True)
    # add image 
 
    #one user has one address, but one address has multiple users
    address = db.relationship("Address", back_populates="users")
    # one activity can have many users.
    activities = db.relationship("Activity", secondary="subscribers", back_populates="users")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}"

class Activity(db.Model):
    """The Activity created by a user and subscribed to by many"""

    __tablename__ = "activities"

    activity_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address_id = db.Column(db.Integer, db.ForeignKey("addresses.address_id"), nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=True) 
    activity_name = db.Column(db.String(25), nullable=False)
    activity_type = db.Column(db.String(25), nullable=False)
    activity_date = db.Column(db.DateTime, nullable=False)
    activity_description = db.Column(db.Text)
    # add image 

    # every activity has one address. One address can be reused for many activities
    address = db.relationship("Address", back_populates="activities")
    #one activity can have many users, and one users can have many activities- hence list of objects will be returned. 
    users = db.relationship("User", secondary="subscribers", back_populates="activities")

    def __repr__(self):
        return f"<Activity activity_id={self.activity_id} activity_name={self.activity_name}"

class Subscriber(db.Model):
    """Association table.Multiple users can sign up for the same activity created by one user. 
    This table hold the user_id and the activity_id for each subscription"""

    __tablename__ = "subscribers"

    subscriber_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    activity_id = db.Column(db.Integer, db.ForeignKey("activities.activity_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    def __repr__(self):
        return f"<This is the subscriber. subscriber_id={self.subscriber_id}"
    
class Address(db.Model):
    """Addresses for activities and users"""
    
    __tablename__ = "addresses" 

    address_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street_num = db.Column(db.Integer, nullable=False)
    suit_num = db.Column(db.Integer, nullable=False)
    street_name = db.Column(db.String(25), nullable=False)
    city = db.Column(db.String(25), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)

    #one user has one address and one address can have multiple user- every user has one address 
    users = db.relationship("User", back_populates="address")
    # one address can be used for many activities
    activities = db.relationship("Activity", back_populates="address")

    def __repr__(self):
        return f"<Address address_id={self.address_id} street_name={self.street_name}"

def connect_to_db(flask_app, db_uri="postgresql:///activity_matcher", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)
         