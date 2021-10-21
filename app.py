import mariadb
from flask import Flask
from endpoints.users import users
from endpoints.tweets import tweets
from endpoints.tweet_likes import tweet_likes
from endpoints.login import login
from endpoints.follows import follows
from endpoints.followers import followers
from endpoints.comments import comments
from endpoints.comment_likes import comment_likes

app = Flask(__name__)

app.register_blueprint(users)
app.register_blueprint(tweets)
app.register_blueprint(tweet_likes)
app.register_blueprint(login)
app.register_blueprint(follows)
app.register_blueprint(followers)
app.register_blueprint(comments)
app.register_blueprint(comment_likes)

app.debug = True

if __name__ == "__main__":
    app.run()