from flask import Blueprint, jsonify, Response, request
from flask.helpers import make_response
from database import db_user_sessions, db_users
from uuid import uuid4

login = Blueprint("/api/login", __name__)

@login.route("/api/login", methods=["POST"])
def user_login():
    try:
        data = request.get_json()
        email = data["email"]
        provided_pword = data["password"]
        user = db_users.get_user_email(email)
        stored_pword = db_users.get_user_password(user[0]["id"])

        if provided_pword == stored_pword:
            db_user_sessions.login_user(user[0]["id"])
            rand_token = uuid4()
            user_id = (user[0]["id"])
            db_user_sessions.update_login_token(str(rand_token), user_id)
            return make_response(jsonify(user), 200)
        else:
            return make_response(jsonify({"message": "Username and/or password do not match"}), 409)
    except Exception as err:
        print(err)
        return make_response(jsonify({"message": "Incorrect data provided"}), 400)

@login.route("/api/login", methods=["DELETE"])
def user_logout():
    user = None
    try:
        data = request.get_json()
        provided_token = data["login_token"]
        user = data["userId"]
        stored_token = db_user_sessions.fetch_login_token(user[0]["users_id"])
        if str(provided_token) == str(stored_token):
            db_user_sessions.logout_user(user[0]["id"])
            return make_response(jsonify(user),200)
    except Exception as err:
        print (err)
        return make_response(jsonify({"message": "Invalid token"}), 400)


    
