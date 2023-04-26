from flask import (Flask, render_template, request, flash, session, redirect)
from model import db,  User, Address, Activity, Subscriber, connect_to_db
import crud as crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "CHANGE THIS"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage(view note)"""
    
    user = None
    if "user_email" in session:
        user = crud.get_user_by_email(session["user_email"])
    
    activities = Activity.query.all()

    return render_template('homepage.html', user = user, activities=activities)

@app.route('/create_new_account')
def show_create_page():
    """View create new account page"""
    return render_template('create_new_account.html')

@app.route("/users", methods=["POST"])
def create_new_user():
    """Create a new user."""
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    street_num = request.form.get("street_num")
    suit_num = request.form.get("suit_num")
    street_name = request.form.get("street_name")
    city = request.form.get("city")
    state = request.form.get("state") 
    zip_code = request.form.get("zip_code")
    user_description = request.form.get("user_description")

    address = crud.create_address(street_num, suit_num, street_name, city, state, zip_code)
    db.session.add(address)
    db.session.commit()

    user = crud.get_user_by_email(email)
    if user:
        flash("An account with that email already exists. Try another email.")
    else:
        user = crud.create_user(username, email, password, fname,lname, address.address_id, user_description)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")

@app.route("/users/<user_id>")
def show_user_profile(user_id):
    """Display details on a particular user."""
    # Query the database for the user with the given user_id
    user = crud.get_user_by_id(user_id)
    # Get the user's activities from the database
    activities = crud.get_activities_by_user(user_id)
    # Render the user_profile.html template with the user and activities data
    return render_template('user_profile.html', user=user, activities=activities)

@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email and name in session
        session["user_email"] = user.email
        session["user_name"] = user.username
        flash(f"Welcome back, {user.username}!")

    return redirect("/")

@app.route("/logout")
def logout():
    """Log out the current user."""

    # Remove the user's email and name from session
    del session["user_email"]
    del session["user_name"]

    # Redirect the user to the homepage
    return redirect("/")

@app.route("/create_new_activity")
def show_create_activities():
    """View create activities"""

    return render_template("create_new_activity.html")

@app.route("/activities")
def create_activities():
    """Create a new activities"""
    activity_name = request.form.get("activity_name")
    activity_type = request.form.get("activity_type")
    activity_date = request.form.get("activity_date")
    activity_description = request.form.get("activity_description")
    created_by = request.form.get("created_by")
    street_num = request.form.get("street_num")
    suit_num = request.form.get("suit_num")
    street_name = request.form.get("street_name")
    city = request.form.get("city")
    state = request.form.get("state") 
    zip_code = request.form.get("zip_code")

    address = crud.create_address(street_num, suit_num, street_name, city, state, zip_code)
    db.session.add(address)
    db.session.commit()

    activity = crud.create_activity(address.address_id, created_by, activity_name, activity_type, activity_date, activity_description)
    db.session.add(activity)
    db.session.commit()
    flash("Yay!! Your activity has been succesfully created!")

    return redirect("/users/<user_id>")

# @app.route("/all_activities")
# def show_all_activities():
#     """View all activities"""

#     activities = Activity.query.all()

#     return render_template("all_activities.html", activities=activities)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

