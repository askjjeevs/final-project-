from flask import (Flask, render_template, request, flash, session, redirect, jsonify, json)
from model import db,  User, Address, Activity, Subscriber, connect_to_db
from datetime import datetime
import crud as crud
import cloudinary.uploader
import os
from passlib.hash import argon2

CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
CLOUD_NAME = "tribeconnect"

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "CHANGE THIS"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """View homepage(view note)"""
    
    user = None
    if "user_id" in session:
        user = crud.get_user_by_id(session["user_id"])
        
    records = [activity.to_json() for activity in Activity.query.all()]

    return render_template('homepage.html', user=user, activities=json.dumps(records))


@app.route("/sign_up_page")
def display_sign_up():
    """View Sign Up page"""
    return render_template('sign_up_page.html')

@app.route("/sign_up_form", methods=["POST"])
def sign_up_new_user():
    """Sign_up a new user"""
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    street_address = (" ")
    city = (" ")
    state = (" ")
    zip_code = (" ")

    user = crud.get_user_by_email(email, argon2.hash(password))
    if user:
        flash("An account with that email already exists. Try another email.")
    else:
        user = crud.create_user(username, email, password, fname,lname, street_address, city, state, zip_code)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/log_in_page")
 
# LOG IN/LOG OUT
@app.route("/log_in_page")
def display_log_in():
    """View Log In page"""
    return render_template('log_in_page.html')

@app.route("/log_in_form", methods=["POST"])
def process_log_in():
    """Process user log in."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or not argon2.verify(password, user.password):
        flash("The email or password you entered was either not in our system or incorrect. Please try again")
        # return redirect('create_account')
        return redirect("/log_in_page")
    else:
        session["user_id"] = user.user_id
        session["user_email"] = user.email
        session["user_name"] = user.username
        flash(f"Welcome back, {user.username}!")

    return redirect("/")

@app.route("/log_out")
def log_out():
    """Log out the current user."""

    del session["user_id"]
    del session["user_email"]
    del session["user_name"]

    return redirect("/")

# USER DASHBOARD AND PROFILE

@app.route("/users/<user_id>")
def display_user_dashboard(user_id):
    """User dashboard displays info about activities and give access to account and profile for a user by user_id."""
    user = crud.get_user_by_id(user_id)
    activities = crud.get_activities_by_user(user_id)
    user_address = crud.get_address_by_user_id(user_id)
    created_activities = crud.get_activities_user_created(user_id)
    return render_template('user_dashboard.html', user=user, activities=activities, user_address=user_address, created_activities=created_activities)

@app.route("/user_profile/<user_id>")
def display_user_profile(user_id):
    """Display details/profile of a particular user by user_id- for other users to view"""

    user = crud.get_user_by_id(user_id)
    activities = crud.get_activities_by_user(user_id)
    created_activities = crud.get_activities_user_created(user_id)

    return render_template('user_profile.html', user=user, activities=activities, created_activities=created_activities)

# USER ACCOUNT 
@app.route("/account_details/<user_id>")
def display_user_account(user_id):
    """The user account is where the user can view and edit all their personal information"""

    user = crud.get_user_by_id(user_id)

    return render_template('account_details.html', user=user)


@app.route('/update_account')
def display_update_account_page():
    """View update account page"""

    user = crud.get_user_by_id(session["user_id"])
   
    return render_template('update_account.html', user=user)

@app.route("/update_account_form", methods=["POST"])
def update_user_account():
    """Update a new account."""

    user_id = request.form.get("user_id")
    user = crud.get_user_by_id(user_id)
    user.username = request.form.get("username")
    user.password = request.form.get("password")
    user.fname = request.form.get("fname")
    user.lname = request.form.get("lname")
    user.address.street_address = request.form.get("street_address")
    user.address.city = request.form.get("city")
    user.address.state = request.form.get("state")
    user.address.zip_code = request.form.get("zip_code")
    user.user_description = request.form.get("user_description")

    my_file = request.files['my-file']
    if my_file:
        user.user_image_path = upload_to_cloudinary(my_file)

    # address = crud.create_address(street_address, city, state, zip_code)
    # user.address.address_id = address.address_id
    # db.session.add(address)
    
    db.session.commit()
    flash("Tribe account updates have been successfully submitted")

    return redirect("/")

# ACTIVITIES
@app.route("/create_new_activity")
def display_create_activities():
    """View create activities"""

    return render_template("create_new_activity.html")

@app.route("/activities", methods=["POST"])
def create_activities():
    """Create a new activities"""

    activity_name = request.form.get("activity_name")
    activity_type = request.form.get("activity_type")
    activity_date = request.form.get("activity_date")
    activity_description = request.form.get("activity_description")
    activity_image_path = '/static/images/default_activity.jpg'
    created_by = int(session["user_id"])
    street_address = request.form.get("street_address")
    city = request.form.get("city")
    state = request.form.get("state") 
    zip_code = request.form.get("zip_code")

    address = crud.create_address(street_address, city, state, zip_code)
    db.session.add(address)
    db.session.commit()

    activity = crud.create_activity(address.address_id, created_by, activity_name, activity_type, activity_date, activity_image_path, activity_description)
    db.session.add(activity)
    db.session.commit()
    flash("Hooray!! Your activity has been succesfully created!")

    return redirect("/users/"+str(session["user_id"]))


@app.route("/messages", methods=["POST"])
def create_activity_message():
    """Create activity message"""
    json = request.get_json()
    activity_id = json.get("activity_id")
    user_id = int(session["user_id"])
    created_datetime = datetime.now()
    message_text = json.get("message_text")

    message = crud.create_message(activity_id, user_id, created_datetime, message_text)
    db.session.add(message)
    db.session.commit()

    return jsonify({'status': 200, 'success': True, "msg": "You have created a message"})


@app.route("/messages/<activity_id>")
def display_activity_message(activity_id):

    messages = crud.get_messages_by_activityId(activity_id)

    records = [message.to_json() for message in messages]

    return jsonify({'status': 200, 'success': True, "messages": records})

@app.route("/update_activity/<activity_id>")
def display_update_activity(activity_id):
    """Display the update activity page"""

    activity = crud.get_activity_by_id(activity_id)

    return render_template("update_activity.html", activity=activity)

@app.route("/update_activities", methods=["POST"])
def update_activities():
    """Update an existing activity if user is the activity creator"""

    activity_id = request.form.get("activity_id")
    activity = crud.get_activity_by_id(activity_id)
    
    activity.activity_name = request.form.get("activity_name")
    activity.activity_type = request.form.get("activity_type")
    activity.activity_date = request.form.get("activity_date")
    activity.activity_description = request.form.get("activity_description")
    
    activity.address.street_address = request.form.get("street_address")
    activity.address.city = request.form.get("city")
    activity.address.state = request.form.get("state")
    activity.address.zip_code = request.form.get("zip_code")

    my_file = request.files['my-file']
    if my_file:
        activity.activity_image_path = upload_to_cloudinary(my_file)

    db.session.commit()
    flash("YES! This activity has been succesfully updated!")

    return redirect("/activities/" + str(activity_id))     

def upload_to_cloudinary(media_file):
    """Upload media file to Cloudinary"""
    result = cloudinary.uploader.upload(media_file,
                                        api_key=CLOUDINARY_KEY,
                                        api_secret=CLOUDINARY_SECRET,
                                        cloud_name=CLOUD_NAME)
    return result['secure_url']

@app.route("/activities/<activity_id>")
def display_activity_details(activity_id):
    """View activity details page"""

    activity = crud.get_activity_by_id(activity_id)
    print("sdfsdfdsfsdf", activity)

    is_logged_in_user_subscribed = False
    if "user_id" in session:
        for user in activity.users:
            if user.user_id == session["user_id"]:
                is_logged_in_user_subscribed = True
    else:
        flash("Please log in to subscribe to activities.")

    return render_template("activity_details.html", activity=activity, is_logged_in_user_subscribed=is_logged_in_user_subscribed)



@app.route("/subscribe/<activity_id>")
def subscribe_activity(activity_id):
    """Users can subscribe to an activity"""

    if "user_id" not in session:
        return jsonify({'success': False, 'msg': "Please log in to subscribe to activities."})

    activity = crud.get_activity_by_id(activity_id)
    if not activity:
        return  jsonify({'success': False, 'msg': "This activity does not exist."})
   
    if activity.creator.user_id==session["user_id"]:
        return jsonify({'success': False,'msg': "You cannot subscribe to an activity you created. Try another"})
    else:
        subscriber = Subscriber(user_id=session["user_id"], activity_id=activity_id)
        db.session.add(subscriber)
        db.session.commit()
    
    return jsonify({'success': True, "msg": "You have subscribed to this activity!"})



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

