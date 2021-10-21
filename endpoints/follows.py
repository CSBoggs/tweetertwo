from flask import Blueprint, jsonify, Response, request
import dbcreds
from database import db_followings, db_users

follows = Blueprint("/api/follows", __name__)

@follows.route("/api/follows", methods=["GET"])
def get_follows():
    pass