@app.route("/sign_up", methods=["POST"])
def sign_up_new_user():
    """Sign_up a new user"""
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    fname = request.form.get("fname")
    lname = request.form.get("lname")

    user = crud.get_user_by_email(email)
    if user:
        flash("An account with that email already exists. Try another email.")
    else:
        user = crud.create_user(username, email, password, fname, lname)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")


@app.route("/log_in_page")
def display_log_in():
    """View Sign Up page"""
    return render_template('log_in_page.html')


@app.route("/login", methods=["POST"])
def process_login():
    """Process user log in."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was either not in our system or incorrect. Please try again")
    else:
        session["user_id"] = user.user_id
        session["user_email"] = user.email
        session["user_name"] = user.username
        flash(f"Welcome back, {user.username}!")

    return redirect("/")


@app.route("/logout")
def logout():
    """Log out the current user."""

    del session["user_id"]
    del session["user_email"]
    del session["user_name"]

    return redirect("/")


@app.route('/update_user_account')
def display_create_account_page():
    """View update account page"""

    return render_template('update_user_account.html')


@app.route("/users", methods=["POST"])
def update_user_account():
    """Create a new account."""
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    street_address = request.form.get("street_address")
    city = request.form.get("city")
    state = request.form.get("state")
    zip_code = request.form.get("zip_code")
    user_image_path = '/static/images/user_profile_stock.jpg'
    user_description = request.form.get("user_description")

    address = crud.create_address(street_address, city, state, zip_code)
    db.session.add(address)
    db.session.commit()

    user = crud.get_user_by_email(email)
    if user:
        flash("An account with that email already exists. Try another email.")

    else:
        db.session.commit()
        flash("Tribe account updates have been successfully submitted")

    return redirect("/")


@app.route("/users/<user_id>")
def display_user_dashboard(user_id):
    """User dashboard displays info about activities and give access to account and profile for a user by user_id."""
    user = crud.get_user_by_id(user_id)
    activities = crud.get_activities_by_user(user_id)
    user_address = crud.get_address_by_user_id(user_id)
    created_activities = crud.get_activities_user_created(user_id)
    return render_template('user_dashboard.html', user=user, activities=activities, user_address=user_address, created_activities=created_activities)


@app.route("/user_account/<user_id>")
def display_user_account(user_id):
    """The user account is where the user can view and edit all their personal information"""

    user = crud.get_user_by_id(user_id)

    return render_template('user_account.html', user=user)


@app.route("/user_profile/<user_id>")
def display_user_profile(user_id):
    """Display details/profile of a particular user by user_id"""

    user = crud.get_user_by_id(user_id)
    activities = crud.get_activities_by_user(user_id)
    created_activities = crud.get_activities_user_created(user_id)

    return render_template('user_profile.html', user=user, activities=activities, created_activities=created_activities)
