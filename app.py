from flask import Flask
import mariadb
from endpoints.users import users

app = Flask(__name__)

app.register_blueprint(users)
app.debug = True

if __name__ == '__main__':
    app.run()