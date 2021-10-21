from flask import Blueprint, jsonify, Response, request
import dbcreds
from database import db_tweet_likes

tweet_likes = Blueprint("/api/tweet-likes", __name__)

@tweet_likes.route("/api/tweet-likes", methods=["GET"])
def get_tweet_likes():
    pass