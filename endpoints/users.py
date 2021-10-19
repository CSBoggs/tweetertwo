from flask import Flask, request, Response, Blueprint
from database import db_users
import json

users = Blueprint('/users', __name__)

@users.route('/users', methods=["GET"])
def get_users():
    userId = None

    try: 
        userId = request.args['userId']
    except Exception:
        print(Exception)
    
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
