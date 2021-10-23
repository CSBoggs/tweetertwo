from flask import Blueprint, jsonify, Response, request
from flask.helpers import make_response
from database import db_tweets, db_user_sessions

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

@tweets.route("/api/tweets", methods=["POST"])
def post_tweet():
    try: 
        data = request.get_json()
        content = data["content"]
        login_token = data["loginToken"]
        user_id = db_user_sessions.fetch_user_id_login_token(login_token)
        new_tweet = db_tweets.post_tweet(user_id, content)
        fresh_tweet = db_tweets.get_tweets_tweet_id(new_tweet)
        return make_response(jsonify(fresh_tweet), 201)
    except Exception as err:
        print(err)
        return Response ("Service unavailable", mimetype="text/plain", status=503)

@tweets.route("/api/tweets", methods=["DELETE"])
def delete_tweet(user_id):
    try:
        data = request.get_json()
        tweet_id = data["tweetId"]
        deleted_tweet = db_tweets.delete_tweet(user_id, tweet_id)
        if deleted_tweet != 1:
            return Response ("Service unavailable", mimetype="text/plain", status=503)
        else:
            return Response ("Tweet content successfully deleted", mimetype="text/plain", status=200)
    except Exception as err:
        print(err)
        return Response ("Service unavailable", mimetype="text/plain", status=503)