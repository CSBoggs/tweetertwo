import dbcreds
import mariadb

def get_user_id(user_id):
    try:
        conn = mariadb.connect(
                            user=dbcreds.user,
                            password=dbcreds.password,
                            host=dbcreds.host,
                            port=dbcreds.port,
                            database=dbcreds.database)
        cursor = conn.cursor()
        user = cursor.execute("SELECT id, username, email, birthdate, bio FROM users WHERE id = ?", [user_id])
        return user
    except mariadb.OperationalError:
        print("something is wrong with the connection")
    finally:
        cursor.close()
        conn.close()

def get_users_all():
    try:
        conn = mariadb.connect(
                            user=dbcreds.user,
                            password=dbcreds.password,
                            host=dbcreds.host,
                            port=dbcreds.port,
                            database=dbcreds.database)
        cursor = conn.cursor()
        users = cursor.execute("SELECT id, username, email, birthdate, bio FROM users")
        return users
    except mariadb.OperationalError:
        print("something is wrong with the connection")
    finally:
        cursor.close()
        conn.close()