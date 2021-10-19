from flask import Flask, request, Response, Blueprint
from app import app_users
import json

users = Blueprint('/api/users',__name__)

@users.route('/api/users', methods=["GET"])
def get_users():
    userId = None

    try: 
        userId = request.args['userId']
    except Exception:
        print(Exception)
    
    if userId:
        user = app_users.get_user_from_id(userId)
        if user:
            resp = Response(
                json.dumps(user, default=str), mimetype="application/json", status=201)
            return resp
        else:
            return Response(
                "User not found", mimetype="text/plain", status=401
            )
    else:
        all = app_users.get_users()
        if not all:
            return Response(
                "No users found", mimetype="text/plain", status=400
            )
        else:
            resp = Response(
                json.dumps(all, default=str), mimetype="application/json", status=200)
            return resp
