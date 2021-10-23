import mariadb
from .db_functions import fetch, connect_to_db
from database import db_user_sessions
from datetime import datetime

def get_tweets_all():
    tweets = fetch("SELECT userTweets.id AS tweetId, user.id as userId, content, created_at, username FROM (SELECT id, username FROM users) AS user JOIN (SELECT * FROM tweets) AS userTweets ON userTweets.users_id = user.id")
    return tweets

def get_tweets_user_id(user_id):
    tweets = fetch("SELECT userTweets.id AS tweetId, user.id as userId, content, created_at, username FROM (SELECT id, username FROM users) AS user JOIN (SELECT * FROM tweets WHERE users_id = (?)) AS userTweets ON userTweets.users_id = user.id", [user_id])
    return tweets

def get_tweets_tweet_id(tweet_id):
    tweet = fetch(" userTweets.id AS tweetId, user.id as userId, content, created_at, username FROM (SELECT id, username FROM users) AS user JOIN (SELECT * FROM tweets WHERE users_id = (?)) AS userTweets ON userTweets.users_id = user.id", [tweet_id])
    return tweet

def post_tweet(user_id, content):
    timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    tweet_id = None
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tweets (users_id, content, created_at) VALUES (?, ?, ?)", user_id, content, timestamp)
        tweet_id = cursor.lastrowid
        conn.commit()
    except mariadb.OperationalError:
        print("something is wrong with the connection")
    finally:
        cursor.close()
        conn.close()
    return tweet_id

def delete_tweet(user_id, tweet_id):
    deleted_tweet = None
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tweets WHERE id = (?)", [tweet_id, user_id])
        deleted_tweet = cursor.rowcount
        conn.commit()
    except mariadb.OperationalError:
        print("something is wrong with the connection")
    finally:
        cursor.close()
        conn.close()
    return deleted_tweet