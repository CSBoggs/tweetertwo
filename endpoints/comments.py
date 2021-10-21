from flask import Blueprint, jsonify, Response, request
import dbcreds
from database import db_comments

comments = Blueprint("/api/comments", __name__)

@comments.route("/api/comments", methods=["GET"])
def get_comments():
    pass