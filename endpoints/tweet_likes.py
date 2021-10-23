from flask import Blueprint, jsonify, make_response, Response, request
from database import db_tweet_likes

tweet_likes = Blueprint("/api/tweet-likes", __name__)

@tweet_likes.route("/api/tweet-likes", methods=["GET"])
def get_tweet_likes():
    tweet_id = None
    if request.args:
        tweet_id = request.args["tweetId"]
    if tweet_id:
        tweet_likes = db_tweet_likes.get_likes_tweet_id(tweet_id)
        return make_response(jsonify(tweet_likes), 200)
    else:
        all = db_tweet_likes.get_likes_all()
        if all:
            return make_response(jsonify(all), 200)
        else:
            return make_response(jsonify({"message": "No likes found"}), 404)