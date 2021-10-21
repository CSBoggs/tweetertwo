from .db_functions import fetch, insert

def login_user(user_id):
    insert("REPLACE INTO user_session (users_id) VALUES (?)", [user_id])

def logout_user(user_id):
    insert("DELETE FROM user_session WHERE users_id = (?)", [user_id])