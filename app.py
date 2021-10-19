import mariadb
import json
from flask import Flask

from api.endpoints.users import users

app = Flask(__name__)

app.register_blueprint(users)

@app.route('/')
def homepage():
    return "backend sucks"