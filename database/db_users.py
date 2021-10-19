import dbcreds
import mariadb
from db_functions import connect_to_db

def get_user_id(user_id):
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        users = cursor.execute("SELECT id, username, email, birthdate, bio FROM users WHERE id = ?", [user_id])
        
        row_headers = [x[0] for x in cursor.description]
        row_values = cursor.fetchall()

        json_data=[]
        for result in row_values:
            json_data.append(dict(zip(row_headers, result)))
        result = json_data
        return users
        
    except mariadb.OperationalError:
        print("something is wrong with the connection")
    finally:
        cursor.close()
        conn.close()

def get_users_all():
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        users = cursor.execute("SELECT * FROM users")
        
        row_headers = [x[0] for x in cursor.description]
        row_values = cursor.fetchall()

        json_data=[]
        for result in row_values:
            json_data.append(dict(zip(row_headers, result)))
        result = json_data
        return users

    except mariadb.OperationalError:
        print("something is wrong with the connection")
    finally:
        cursor.close()
        conn.close()