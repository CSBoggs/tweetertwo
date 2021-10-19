from mariadb import connect
import dbcreds

connection = None
cursor = None

def connect_to_db():
    return connect(
        user=dbcreds.user,
        password=dbcreds.password,
        host=dbcreds.host,
        port=dbcreds.port,
        database=dbcreds.database
    )