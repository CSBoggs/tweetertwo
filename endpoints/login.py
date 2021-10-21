from flask import Blueprint, jsonify, Response, request
import dbcreds
from database import db_sessions, db_users

login = Blueprint("/api/login", __name__)

@login.route("/api/login", methods=["POST"])
def user_login():
    pass