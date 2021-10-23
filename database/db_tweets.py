from .db_functions import fetch

def get_tweets_all():
    tweets = fetch("SELECT userTweets.id AS tweetId, user.id as userId, content, created_at, username FROM (SELECT id, username FROM users) AS user JOIN (SELECT * FROM tweets) AS userTweets ON userTweets.users_id = user.id")
    return tweets

def get_tweets_user_id(user_id):
    tweets = fetch("SELECT userTweets.id AS tweetId, user.id as userId, content, created_at, username FROM (SELECT id, username FROM users) AS user JOIN (SELECT * FROM tweets WHERE users_id = (?)) AS userTweets ON userTweets.users_id = user.id", [user_id])
    return tweets

def get_tweets_id(tweet_id):
    tweet = fetch(" userTweets.id AS tweetId, user.id as userId, content, created_at, username FROM (SELECT id, username FROM users) AS user JOIN (SELECT * FROM tweets WHERE users_id = (?)) AS userTweets ON userTweets.users_id = user.id", [tweet_id])
    return tweet
