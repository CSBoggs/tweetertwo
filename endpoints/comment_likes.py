from flask import Blueprint, jsonify, Response, request
import dbcreds
from database import db_comment_likes

comment_likes = Blueprint("/api/comment-likes", __name__)

@comment_likes.route("/api/comment-likes", methods=["GET"])
def get_comment_likes():
    pass