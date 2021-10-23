from .db_functions import connect_to_db, fetch, insert

def get_likes_tweet_id(tweet_id):
    likes = fetch("SELECT tweetId, userId, username FROM (SELECT id, username FROM users) AS user JOIN (SELECT tweet_id AS tweetId, users_id AS userId FROM tweet_likes WHERE tweet_id = (?)) AS tweet_likes ON tweet_likes.userId = user.id", [tweet_id])
    return likes

def get_likes_all():
    likes = fetch("SELECT tweetId, userId, username FROM (SELECT id, username FROM users) AS user JOIN (SELECT tweet_id as tweetId, users_id as userId FROM tweet_likes) AS tweet_likes ON tweet_likes.userId = user.id")
    return likes