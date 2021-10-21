from flask import Blueprint, jsonify, Response, request
import dbcreds
from database import db_tweets

tweets = Blueprint("/api/tweets", __name__)

@tweets.route("/api/tweets", methods=["GET"])
def get_tweets():
    pass