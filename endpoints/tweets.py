from flask import Blueprint, jsonify, Response, request
from flask.helpers import make_response
from database import db_tweets

tweets = Blueprint("/api/tweets", __name__)

@tweets.route("/api/tweets", methods=["GET"])
def get_tweets():
    user_id = None
    if request.args:
        user_id = request.args["userId"]
    if user_id:
        user_tweets = db_tweets.get_tweets_user_id(user_id)
        if user_tweets:
            return make_response(jsonify(user_tweets), 200)
        else:
            return make_response(jsonify({"message": "No tweets found with provided user ID"}), 401)
    else:
        all = db_tweets.get_tweets_all()
        if not all:
            return make_response(jsonify({"message": "No tweets found"}), 401)
        else:
            return make_response(jsonify(all), 200)