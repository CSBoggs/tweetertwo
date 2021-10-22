import mariadb
from .db_functions import connect_to_db, fetch

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

def create_user(username, password, email, birthdate, bio):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, email, birthdate, bio) VALUES (?, ?, ?, ?, ?)", [username, password, email, birthdate, bio])
        conn.commit()
    except mariadb.OperationalError:
        print("something is wrong with the connection")
    else:
        cursor.close()
        conn.close()

def edit_user(user_id, data):
    if data.fetch("username"):
        try:
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET username = (?) WHERE id = (?)", [data["username"], user_id])
            conn.commit()
        finally:
            cursor.close()
            conn.close()
    if data.fetch("email"):
        try:
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET email = (?) WHERE id = (?)", [data["email"], user_id])
            conn.commit()
        finally:
            cursor.close()
            conn.close()
    if data.fetch("birthdate"):
        try:
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET birthdate = (?) WHERE id = (?)", [data["birthdate"], user_id])
            conn.commit()
        finally:
            cursor.close()
            conn.close()
    if data.fetch("bio"):
        try:
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET bio = (?) WHERE id = (?)", [data["bio"], user_id])
            conn.commit()
        finally:
            cursor.close()
            conn.close()

def get_user_password(user_id):
    result = fetch("SELECT password FROM users WHERE id = (?)", [user_id])
    password = result[0]["password"]
    print(password)
    return password

