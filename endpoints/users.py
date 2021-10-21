from flask import Flask, request, make_response, Response, Blueprint
from flask.json import jsonify
from database import db_users
import json
from datetime import datetime

users = Blueprint('/api/users', __name__)

@users.route('/api/users', methods=["GET"])
def get_users():
    userId = None

    try: 
        userId = request.args['userId']
    except Exception as err:
        print(err)
    
    if userId:
        user = db_users.get_user_id(userId)
        if user:
            return make_response(jsonify(user), 200)
        else:
            return make_response(jsonify({"message": "User was not found with that user ID"}), 400)
    else:
        all = db_users.get_users_all()
        if not all:
            return make_response(jsonify({"message": "No users found"}), 400)
        else:
            return make_response(jsonify(all), 200)

@users.route("/api/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        email = data["email"]
        birthdate = datetime.strptime(data["birthdate"], "%Y-%m-%d")
        bio = data["bio"]
        
        try:
            existing_user = db_users.get_user_email(email) or db_users.get_user_username(username)
            if existing_user:
                return make_response(jsonify({"message": "Incorrect data provided"}), 400)
        except:
            pass
    except:
        return make_response(jsonify({"message": "Incorrect data provided"}), 400)
    else:
        db_users.create_user(username, password, email, birthdate, bio)
        created_user = db_users.get_user_username(username)
        return make_response(jsonify(created_user), 201)

@users.route("/api/users", methods=["PATCH"])
def edit_user(user_id):
    data = request.get_json()
    params = {"username", "email", "birthdate", "bio"}
    edit_data = [0] in params, data.items()

    if edit_data:
        db_users.edit_user(user_id, data)
    else:
        return make_response(jsonify({"message": "Incorrect data provided"}), 400)
    return make_response(jsonify({"message": "Updated user information"}), 201)