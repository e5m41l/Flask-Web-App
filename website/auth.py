from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    return "<p>logged!</p>"

@auth.route("/logout")
def logout():
    return "<p>logged out!</p>"

@auth.route("/sign-up")
def signup():
    return "<p>sign-up!</p>"
