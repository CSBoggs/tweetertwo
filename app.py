import mariadb
import json
from flask import Flask
from app import app
from api.endpoints.users import users

app = Flask(__name__)

app.register_blueprint(users)
app.debug = True

@app.route('/')
def homepage():
    return "backend sucks"

if __name__ == '__main__':
    app.run()