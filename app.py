import os

from flask import Flask, request, send_from_directory, redirect
from pymongo import MongoClient
from flask_login import LoginManager, login_user, login_required

from models import User

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY").encode()

login = LoginManager(app)
login.login_view = 'login'

def get_database(dbname):
    CONNECTION_STRING = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
    return client[dbname]

@login.user_loader
def load_user(username):
    db = get_database("user_auth_tutorial")
    users_collection = db["users"]
    return User(users_collection, username)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return send_from_directory("static", "login.html")

    elif request.method == 'POST':
        username = request.form['username']
        incoming_password = request.form['password']
        print(f"attempting to login as: {username}")

        db = get_database("user_auth_tutorial")
        users_collection = db["users"]

        try:
            found_user = User(users_collection, username)

            if found_user.check_password(incoming_password):
                login_user(found_user)
                return redirect("/private")
            else:
                return "Invalid Username or Password"

        except ValueError:
            return "Invalid Username or Password"


@app.route('/')
def index():  # put application's code here

    # db = get_database("user_auth_tutorial")
    # users_collection = db["users"]
    # print(list(users_collection.find({"username": "foamyguy"})))

    return 'Public page that anyone is allowed to see'

@app.route('/private')
@login_required
def private_page():  # put application's code here
    return 'Private page that you must be logged in to see!!'

if __name__ == '__main__':
    app.run()
