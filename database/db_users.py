import mariadb
from .db_functions import connect_to_db

def get_user_id(user_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, birthdate, bio FROM users WHERE id = ?", [user_id])
        
        row_headers = [x[0] for x in cursor.description]
        row_values = cursor.fetchall()

        json_data=[]
        for result in row_values:
            json_data.append(dict(zip(row_headers, result)))
        result = json_data
        return result
        
    except mariadb.OperationalError:
        print("something is wrong with the connection")
    finally:
        cursor.close()
        conn.close()

def get_user_email(email):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, birthdate, bio FROM users WHERE email = ?", [email])
        
        row_headers = [x[0] for x in cursor.description]
        row_values = cursor.fetchall()

        json_data=[]
        for result in row_values:
            json_data.append(dict(zip(row_headers, result)))
        result = json_data
        return result
        
    except mariadb.OperationalError:
        print("something is wrong with the connection")
    finally:
        cursor.close()
        conn.close()

def get_user_username(username):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, birthdate, bio FROM users WHERE username = ?", [username])
        
        row_headers = [x[0] for x in cursor.description]
        row_values = cursor.fetchall()

        json_data=[]
        for result in row_values:
            json_data.append(dict(zip(row_headers, result)))
        result = json_data
        return result
        
    except mariadb.OperationalError:
        print("something is wrong with the connection")
    finally:
        cursor.close()
        conn.close()

def get_users_all():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email, birthdate, bio FROM users")
        
        row_headers = [x[0] for x in cursor.description]
        row_values = cursor.fetchall()

        json_data=[]
        for result in row_values:
            json_data.append(dict(zip(row_headers, result)))
        result = json_data
        return result
        
    except mariadb.OperationalError:
        print("something is wrong with the connection")
    finally:
        cursor.close()
        conn.close()

def create_user(username, email, password, birthdate, bio):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, email, password, birthdate, bio) VALUES (?, ?, ?, ?, ?)", [username, email, password, birthdate, bio])
        conn.commit()
    except Exception as e:
        print(e)
    else:
        cursor.close()
        conn.close()