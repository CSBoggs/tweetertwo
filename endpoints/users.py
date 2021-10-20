from flask import Flask, request, Response, Blueprint
from database import db_users
import json
from datetime import datetime

users = Blueprint('/api/users', __name__)

@users.route('/api/users', methods=["GET"])
def get_users():
    userId = None

    try: 
        userId = request.args['userId']
    except Exception as e:
        print(e)
    
    if userId:
        user = db_users.get_user_id(userId)
        if user:
            resp = Response(
                json.dumps(user, default=str), mimetype="application/json", status=201)
            return resp
        else:
            return Response(
                "User not found", mimetype="text/plain", status=401
            )
    else:
        all = db_users.get_users_all()
        if not all:
            return Response(
                "No users found", mimetype="text/plain", status=400
            )
        else:
            resp = Response(
                json.dumps(all, default=str), mimetype="application/json", status=200)
            return resp

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
                return Response(
                    "Username and/or Email is in use", mimetype="text/plain", status=400
                )
        except:
            pass
    except:
        return Response(
            "Incorrect data provided", mimetype="text/plain", status=400
        )
    else:
        db_users.create_user(username, password, email, birthdate, bio)
        created_user = db_users.get_user_username(username)
        resp = Response(
            json.dumps(created_user, default=str), mimetype="application/json", status=201)
        return resp

@users.route("/api/users", methods=["PATCH"])
def edit_user(user_id):
    data = request.get_json()
    params = {"username", "email", "birthdate", "bio"}
    edit_data = [0] in params, data.items()

    if edit_data:
        db_users.edit_user(user_id, data)
    else:
        return Response(
            "Incorrect data provided", mimetype="text/plain", status=400
        )
    resp = Response(
        json.dumps(edit_data, default=str), mimetype="application/json", status=201)
    return resp