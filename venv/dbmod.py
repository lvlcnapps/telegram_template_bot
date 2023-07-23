import sqlite3
from sqlite3 import Error

create_users_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT NOT NULL, mark INTEGER, description TEXT NOT NULL)"

del_all = """
    drop table likes
"""


def create_connection(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return conn


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def add_line(id_n, name, mark, desc):
    connection = create_connection("C:\\Users\\Admin\\PycharmProjects\\tgbot_2\\venv\\sm_app.sqlite")
    create_users = f'INSERT INTO users (id, name, mark, description) VALUES ({id_n}, "{name}", {mark}, "{desc}")'
    execute_query(connection, create_users)
    return


def show_all():
    connection = create_connection("C:\\Users\\Admin\\PycharmProjects\\tgbot_2\\venv\\sm_app.sqlite")
    print("1")
    select_users = "SELECT * from users"
    users = execute_read_query(connection, select_users)
    for user in users:
        print(user)
    return

# connection = create_connection("C:\\Users\\Admin\\PycharmProjects\\tgbot_2\\venv\\sm_app.sqlite")

# execute_query(connection, create_users_table)
# execute_query(connection, create_posts_table)
# execute_query(connection, create_comments_table)
# execute_query(connection, create_likes_table)

# execute_query(connection, create_users)
# execute_query(connection, create_posts)
# execute_query(connection, create_comments)
# execute_query(connection, create_likes)

# select_users = "SELECT * from users"
# users = execute_read_query(connection, select_users)

# for user in users:
# print(user)
