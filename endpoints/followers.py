from flask import Blueprint, jsonify, Response, request
import dbcreds
from database import db_followers, db_users

followers = Blueprint("/api/followers", __name__)

@followers.route("/api/followers", methods=["GET"])
def get_followers():
    pass