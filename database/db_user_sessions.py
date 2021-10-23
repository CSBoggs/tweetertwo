from .db_functions import fetch, insert

def login_user(user_id):
    insert("REPLACE INTO user_session (users_id) VALUES (?)", [user_id])

def logout_user(user_id):
    insert("DELETE FROM user_session WHERE users_id = (?)", [user_id])

def fetch_login_token(user_id):
    result = fetch("SELECT login_token FROM user_session WHERE users_id = (?)", [user_id])
    token = result[0]["login_token"]
    return token

def fetch_user_id_login_token(login_token):
    result = fetch("SELECT users_id FROM user_session WHERE login_token= (?)", [login_token])
    user_id = result[0]["users_id"]
    return user_id

def update_login_token(login_token, user_id):
    insert("UPDATE user_session SET login_token = (?) WHERE users_id = (?)", [login_token, user_id])
