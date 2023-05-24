# TRIBE CONNECT

## Build Your Tribe, One Connection at a Time!

---

### Project Description

Tribe Connect is a web app that simplifies the process of making friends and building a community. On Tribe Connect's homepage, visitors can explore various community activities created by its members. Signing up is a breeze, as it generates a new user account securely stored in the database. Tribe Connect empowers users to create activities and associate images. In cases where users don't provide images, default ones are displayed. The user dashboard allows easy access for editing profiles, creating new activities, and browsing activities created by other users. Activities created by users are open for subscription, and users can also unsubscribe as needed. Additionally, users can connect with activity creators by sending them direct messages.

---

### Tech Stack

#### Frontend:

- HTML
- CSS
- Bootstrap
- JavaScript
- React
- Jinja2

#### Backend:

- Python
- Flask
- PostgreSQL
- SQLAlchemy

#### API:

- Cloudinary

---

### Features

#### Easy User Log In, Sign Up, Log Out

Users can effortlessly log in to their accounts, granting them access to the user dashboard. From there, they can edit their profiles, create new activities, and view the activities they are hosting or subscribed to.

![Log In GIF](/static/gifs/log_in.gif)

#### Update Profile and Activity Feature

Users can easily update their existing profiles and personalize their images by replacing the default ones. These changes can be made directly from the user dashboard.

![Update Image and Profile GIF](/static/gifs/updateimage.gif)

#### Subscribe and Unsubscribe from Activities

Users have the flexibility to explore all activities and choose which ones they want to subscribe to. They can also unsubscribe from activities they are no longer interested in.

![Subscribe GIF](/static/gifs/subscribe.gif)

#### Messaging Activity Host

Logged-in users can communicate with activity hosts by sending messages directly through the web app. This feature enables seamless coordination and interaction among users.

![Messages GIF](/static/gifs/messages.gif)

#### Filter by Activity Type

To streamline the activity browsing experience, users can filter activities based on their preferred activity types. By simply clicking on the desired type, users can quickly find activities that match their interests.

![Filter GIF](/static/gifs/filter.gif)

---

### Run the Tribe Connect Flask App

1. Set up and activate a Python virtual environment and install all dependencies:
    ```
    virtualenv env
    source env/bin/activate
    pip3 install -r requirements.txt
    ```

2. To source Cloudinary:
    ```
    source secret.sh
    ```

3. To create the database and populate it with sample data, run:
    ```
    python3 seed_database.py
    ```

4. Start the Flask server:
    ```
    python3 server.py
    ```

5. Open your browser and go to `localhost:5000` to access the web app.

