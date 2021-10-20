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
        email = data["email"]
        username = data["username"]
        bio = data["bio"]
        birthdate = datetime.strptime(data["birthdate"], "%Y-%m-%d")
        password = data["password"]

        try:
            existing_user = db_users.get_user_email(email) or db_users.get_user_username(username)
            if existing_user == True:
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
        db_users.create_user(username, email, password, birthdate, bio)
        user = db_users.get_user_username(username)
        resp = Response(
            json.dumps(user, default=str), mimetype="application/json", status=201)
        return resp        